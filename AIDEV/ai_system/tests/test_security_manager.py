import pytest
import os
import json
import tempfile
from datetime import datetime, timedelta
import jwt
from ai_system.security.security_manager import SecurityManager

@pytest.fixture
def security_manager():
    """Create a security manager instance for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config = {
            "security_dir": temp_dir,
            "log_dir": temp_dir
        }
        manager = SecurityManager(config)
        yield manager

@pytest.fixture
def sample_user():
    """Create a sample user for testing."""
    return {
        "username": "testuser",
        "password": "testpass123",
        "role": "user"
    }

def test_initialize_security(security_manager):
    """Test security initialization."""
    assert security_manager.encryption_key is not None
    assert security_manager.jwt_secret is not None
    assert security_manager.users == {}
    assert "admin" in security_manager.rbac
    assert "user" in security_manager.rbac
    assert "guest" in security_manager.rbac

def test_create_user(security_manager, sample_user):
    """Test user creation."""
    # Create user
    assert security_manager.create_user(
        sample_user["username"],
        sample_user["password"],
        sample_user["role"]
    )
    
    # Verify user exists
    assert sample_user["username"] in security_manager.users
    user = security_manager.users[sample_user["username"]]
    assert user["role"] == sample_user["role"]
    assert "password_hash" in user
    assert "created_at" in user

def test_authenticate_user(security_manager, sample_user):
    """Test user authentication."""
    # Create user
    security_manager.create_user(
        sample_user["username"],
        sample_user["password"],
        sample_user["role"]
    )
    
    # Test valid authentication
    token = security_manager.authenticate(
        sample_user["username"],
        sample_user["password"]
    )
    assert token is not None
    
    # Test invalid password
    assert security_manager.authenticate(
        sample_user["username"],
        "wrongpass"
    ) is None
    
    # Test non-existent user
    assert security_manager.authenticate(
        "nonexistent",
        "password"
    ) is None

def test_authorize_user(security_manager, sample_user):
    """Test user authorization."""
    # Create user
    security_manager.create_user(
        sample_user["username"],
        sample_user["password"],
        sample_user["role"]
    )
    
    # Get token
    token = security_manager.authenticate(
        sample_user["username"],
        sample_user["password"]
    )
    
    # Test valid authorization
    assert security_manager.authorize(token, "read")
    assert security_manager.authorize(token, "write")
    
    # Test invalid permission
    assert not security_manager.authorize(token, "admin")
    
    # Test invalid token
    assert not security_manager.authorize("invalid_token", "read")

def test_encrypt_decrypt_data(security_manager):
    """Test data encryption and decryption."""
    # Test data
    data = b"test data for encryption"
    
    # Encrypt
    encrypted = security_manager.encrypt_data(data)
    assert encrypted != data
    
    # Decrypt
    decrypted = security_manager.decrypt_data(encrypted)
    assert decrypted == data

def test_update_user(security_manager, sample_user):
    """Test user update."""
    # Create user
    security_manager.create_user(
        sample_user["username"],
        sample_user["password"],
        sample_user["role"]
    )
    
    # Update password
    assert security_manager.update_user(
        sample_user["username"],
        {"password": "newpass123"}
    )
    
    # Verify new password works
    assert security_manager.authenticate(
        sample_user["username"],
        "newpass123"
    ) is not None
    
    # Update role
    assert security_manager.update_user(
        sample_user["username"],
        {"role": "admin"}
    )
    
    # Verify role update
    user = security_manager.users[sample_user["username"]]
    assert user["role"] == "admin"
    assert "updated_at" in user

def test_delete_user(security_manager, sample_user):
    """Test user deletion."""
    # Create user
    security_manager.create_user(
        sample_user["username"],
        sample_user["password"],
        sample_user["role"]
    )
    
    # Delete user
    assert security_manager.delete_user(sample_user["username"])
    
    # Verify user is gone
    assert sample_user["username"] not in security_manager.users
    
    # Try to delete non-existent user
    assert not security_manager.delete_user("nonexistent")

def test_save_and_load_state(security_manager, sample_user):
    """Test state persistence."""
    # Create user
    security_manager.create_user(
        sample_user["username"],
        sample_user["password"],
        sample_user["role"]
    )
    
    # Save state
    state_file = os.path.join(security_manager.config["security_dir"], "state.json")
    security_manager.save_state(state_file)
    
    # Create new manager
    new_manager = SecurityManager(security_manager.config)
    
    # Load state
    new_manager.load_state(state_file)
    
    # Verify state
    assert new_manager.users == security_manager.users
    assert new_manager.rbac == security_manager.rbac

def test_token_expiration(security_manager, sample_user):
    """Test JWT token expiration."""
    # Create user
    security_manager.create_user(
        sample_user["username"],
        sample_user["password"],
        sample_user["role"]
    )
    
    # Get token
    token = security_manager.authenticate(
        sample_user["username"],
        sample_user["password"]
    )
    
    # Decode token
    payload = jwt.decode(
        token,
        security_manager.jwt_secret,
        algorithms=["HS256"]
    )
    
    # Verify expiration
    exp = datetime.fromtimestamp(payload["exp"])
    now = datetime.utcnow()
    assert exp > now
    assert exp - now < timedelta(hours=25)  # Should be less than 24 hours + buffer

def test_password_hashing(security_manager):
    """Test password hashing and verification."""
    password = "testpass123"
    
    # Hash password
    hashed = security_manager._hash_password(password)
    
    # Verify format
    assert ":" in hashed
    salt, key = hashed.split(":")
    assert len(base64.b64decode(salt)) == 16
    assert len(base64.b64decode(key)) == 32
    
    # Verify password
    assert security_manager._verify_password(password, hashed)
    assert not security_manager._verify_password("wrongpass", hashed) 