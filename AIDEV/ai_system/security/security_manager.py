from typing import Any, Dict, List, Optional
import os
import json
import logging
import hashlib
import hmac
import base64
import secrets
from datetime import datetime, timedelta
import jwt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SecurityManager:
    """
    Manager for handling security operations including authentication,
    authorization, encryption, and secure storage.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the security manager.
        
        Args:
            config (Dict[str, Any]): Configuration dictionary
        """
        self.config = config
        self.logger = self._setup_logging()
        self._initialize_security()
        
    def _setup_logging(self) -> logging.Logger:
        """
        Setup logging configuration.
        
        Returns:
            logging.Logger: Configured logger
        """
        logger = logging.getLogger("security_manager")
        logger.setLevel(logging.INFO)
        
        # Create handlers
        file_handler = logging.FileHandler("logs/security_manager.log")
        console_handler = logging.StreamHandler()
        
        # Create formatters
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
        
    def _initialize_security(self) -> None:
        """Initialize security settings and keys."""
        try:
            # Generate or load encryption key
            self.encryption_key = self._get_or_generate_key("encryption_key")
            self.fernet = Fernet(self.encryption_key)
            
            # Generate or load JWT secret
            self.jwt_secret = self._get_or_generate_key("jwt_secret")
            
            # Initialize user store
            self.users = self._load_users()
            
            # Initialize role-based access control
            self.rbac = self._load_rbac()
            
        except Exception as e:
            self.logger.error(f"Error initializing security: {str(e)}")
            raise
            
    def _get_or_generate_key(self, key_name: str) -> bytes:
        """
        Get existing key or generate new one.
        
        Args:
            key_name (str): Name of the key
            
        Returns:
            bytes: Key bytes
        """
        key_path = os.path.join(self.config["security_dir"], f"{key_name}.key")
        
        if os.path.exists(key_path):
            with open(key_path, "rb") as f:
                return f.read()
                
        # Generate new key
        if key_name == "encryption_key":
            key = Fernet.generate_key()
        else:
            key = secrets.token_bytes(32)
            
        # Save key
        os.makedirs(os.path.dirname(key_path), exist_ok=True)
        with open(key_path, "wb") as f:
            f.write(key)
            
        return key
        
    def _load_users(self) -> Dict[str, Dict[str, Any]]:
        """
        Load user data from storage.
        
        Returns:
            Dict[str, Dict[str, Any]]: User data
        """
        users_path = os.path.join(self.config["security_dir"], "users.json")
        
        if os.path.exists(users_path):
            with open(users_path, "r") as f:
                return json.load(f)
                
        return {}
        
    def _load_rbac(self) -> Dict[str, List[str]]:
        """
        Load role-based access control data.
        
        Returns:
            Dict[str, List[str]]: RBAC data
        """
        rbac_path = os.path.join(self.config["security_dir"], "rbac.json")
        
        if os.path.exists(rbac_path):
            with open(rbac_path, "r") as f:
                return json.load(f)
                
        return {
            "admin": ["*"],
            "user": ["read", "write"],
            "guest": ["read"]
        }
        
    def authenticate(self, username: str, password: str) -> Optional[str]:
        """
        Authenticate a user.
        
        Args:
            username (str): Username
            password (str): Password
            
        Returns:
            Optional[str]: JWT token if authentication successful
        """
        try:
            if username not in self.users:
                return None
                
            user = self.users[username]
            stored_hash = user["password_hash"]
            
            # Verify password
            if not self._verify_password(password, stored_hash):
                return None
                
            # Generate JWT token
            token = self._generate_token(username, user["role"])
            
            self.logger.info(f"User {username} authenticated successfully")
            return token
            
        except Exception as e:
            self.logger.error(f"Error authenticating user: {str(e)}")
            return None
            
    def authorize(self, token: str, required_permission: str) -> bool:
        """
        Authorize a user based on their token and required permission.
        
        Args:
            token (str): JWT token
            required_permission (str): Required permission
            
        Returns:
            bool: True if authorized
        """
        try:
            # Verify token
            payload = self._verify_token(token)
            if not payload:
                return False
                
            username = payload["username"]
            role = payload["role"]
            
            # Check permissions
            if role not in self.rbac:
                return False
                
            permissions = self.rbac[role]
            if "*" in permissions or required_permission in permissions:
                return True
                
            return False
            
        except Exception as e:
            self.logger.error(f"Error authorizing user: {str(e)}")
            return False
            
    def encrypt_data(self, data: bytes) -> bytes:
        """
        Encrypt data using Fernet symmetric encryption.
        
        Args:
            data (bytes): Data to encrypt
            
        Returns:
            bytes: Encrypted data
        """
        try:
            return self.fernet.encrypt(data)
        except Exception as e:
            self.logger.error(f"Error encrypting data: {str(e)}")
            raise
            
    def decrypt_data(self, encrypted_data: bytes) -> bytes:
        """
        Decrypt data using Fernet symmetric encryption.
        
        Args:
            encrypted_data (bytes): Data to decrypt
            
        Returns:
            bytes: Decrypted data
        """
        try:
            return self.fernet.decrypt(encrypted_data)
        except Exception as e:
            self.logger.error(f"Error decrypting data: {str(e)}")
            raise
            
    def create_user(self, username: str, password: str, role: str = "user") -> bool:
        """
        Create a new user.
        
        Args:
            username (str): Username
            password (str): Password
            role (str): User role
            
        Returns:
            bool: True if user created successfully
        """
        try:
            if username in self.users:
                return False
                
            # Hash password
            password_hash = self._hash_password(password)
            
            # Create user
            self.users[username] = {
                "password_hash": password_hash,
                "role": role,
                "created_at": datetime.now().isoformat()
            }
            
            # Save users
            self._save_users()
            
            self.logger.info(f"User {username} created successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error creating user: {str(e)}")
            return False
            
    def update_user(self, username: str, updates: Dict[str, Any]) -> bool:
        """
        Update user information.
        
        Args:
            username (str): Username
            updates (Dict[str, Any]): Updates to apply
            
        Returns:
            bool: True if user updated successfully
        """
        try:
            if username not in self.users:
                return False
                
            user = self.users[username]
            
            # Update fields
            if "password" in updates:
                user["password_hash"] = self._hash_password(updates["password"])
            if "role" in updates:
                user["role"] = updates["role"]
                
            user["updated_at"] = datetime.now().isoformat()
            
            # Save users
            self._save_users()
            
            self.logger.info(f"User {username} updated successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error updating user: {str(e)}")
            return False
            
    def delete_user(self, username: str) -> bool:
        """
        Delete a user.
        
        Args:
            username (str): Username
            
        Returns:
            bool: True if user deleted successfully
        """
        try:
            if username not in self.users:
                return False
                
            del self.users[username]
            
            # Save users
            self._save_users()
            
            self.logger.info(f"User {username} deleted successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error deleting user: {str(e)}")
            return False
            
    def _hash_password(self, password: str) -> str:
        """
        Hash a password using PBKDF2.
        
        Args:
            password (str): Password to hash
            
        Returns:
            str: Hashed password
        """
        salt = secrets.token_bytes(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = base64.b64encode(kdf.derive(password.encode()))
        return f"{base64.b64encode(salt).decode()}:{key.decode()}"
        
    def _verify_password(self, password: str, stored_hash: str) -> bool:
        """
        Verify a password against its hash.
        
        Args:
            password (str): Password to verify
            stored_hash (str): Stored hash
            
        Returns:
            bool: True if password matches
        """
        try:
            salt, key = stored_hash.split(":")
            salt = base64.b64decode(salt)
            key = base64.b64decode(key)
            
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000
            )
            verify_key = kdf.derive(password.encode())
            
            return hmac.compare_digest(key, verify_key)
            
        except Exception:
            return False
            
    def _generate_token(self, username: str, role: str) -> str:
        """
        Generate a JWT token.
        
        Args:
            username (str): Username
            role (str): User role
            
        Returns:
            str: JWT token
        """
        payload = {
            "username": username,
            "role": role,
            "exp": datetime.utcnow() + timedelta(hours=24)
        }
        return jwt.encode(payload, self.jwt_secret, algorithm="HS256")
        
    def _verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Verify a JWT token.
        
        Args:
            token (str): JWT token
            
        Returns:
            Optional[Dict[str, Any]]: Token payload if valid
        """
        try:
            return jwt.decode(token, self.jwt_secret, algorithms=["HS256"])
        except Exception:
            return None
            
    def _save_users(self) -> None:
        """Save user data to storage."""
        users_path = os.path.join(self.config["security_dir"], "users.json")
        with open(users_path, "w") as f:
            json.dump(self.users, f, indent=2)
            
    def save_state(self, filepath: str) -> None:
        """
        Save manager state to file.
        
        Args:
            filepath (str): Path to save state
        """
        try:
            state = {
                "config": self.config,
                "users": self.users,
                "rbac": self.rbac
            }
            with open(filepath, 'w') as f:
                json.dump(state, f)
            self.logger.info(f"State saved to {filepath}")
        except Exception as e:
            self.logger.error(f"Error saving state: {str(e)}")
            
    def load_state(self, filepath: str) -> None:
        """
        Load manager state from file.
        
        Args:
            filepath (str): Path to load state from
        """
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
            self.config = state["config"]
            self.users = state["users"]
            self.rbac = state["rbac"]
            self.logger.info(f"State loaded from {filepath}")
        except Exception as e:
            self.logger.error(f"Error loading state: {str(e)}") 