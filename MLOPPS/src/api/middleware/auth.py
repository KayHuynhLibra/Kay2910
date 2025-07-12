from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import os

from ..schemas.auth import TokenData, User
from ..utils.exceptions import AuthenticationError
from ...utils.security.token import TokenManager
from ...utils.security.permissions import PermissionChecker

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class AuthMiddleware:
    """Middleware xác thực"""

    def __init__(self):
        self.token_manager = TokenManager()
        self.permission_checker = PermissionChecker()

    async def get_current_user(
        self,
        token: str = Depends(oauth2_scheme)
    ) -> User:
        """
        Lấy thông tin người dùng hiện tại từ token
        
        Args:
            token: JWT token
            
        Returns:
            User: Thông tin người dùng
            
        Raises:
            HTTPException: Lỗi xác thực
        """
        try:
            # Verify token
            payload = self.token_manager.verify_token(token)
            if payload is None:
                raise AuthenticationError("Invalid token")
                
            # Get user data
            user_id: str = payload.get("sub")
            if user_id is None:
                raise AuthenticationError("Invalid token payload")
                
            # Get user from database
            user = await self.get_user(user_id)
            if user is None:
                raise AuthenticationError("User not found")
                
            return user
            
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except AuthenticationError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
                headers={"WWW-Authenticate": "Bearer"},
            )

    async def get_current_active_user(
        self,
        current_user: User = Depends(get_current_user)
    ) -> User:
        """
        Kiểm tra người dùng có active không
        
        Args:
            current_user: Người dùng hiện tại
            
        Returns:
            User: Thông tin người dùng
            
        Raises:
            HTTPException: Người dùng không active
        """
        if not current_user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )
        return current_user

    async def check_permissions(
        self,
        required_permissions: list[str],
        current_user: User = Depends(get_current_active_user)
    ) -> None:
        """
        Kiểm tra quyền của người dùng
        
        Args:
            required_permissions: Danh sách quyền cần thiết
            current_user: Người dùng hiện tại
            
        Raises:
            HTTPException: Không có quyền truy cập
        """
        if not self.permission_checker.has_permissions(
            current_user,
            required_permissions
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )

    async def get_user(self, user_id: str) -> Optional[User]:
        """
        Lấy thông tin người dùng từ database
        
        Args:
            user_id: ID của người dùng
            
        Returns:
            Optional[User]: Thông tin người dùng
        """
        # TODO: Implement database query
        return None

# Create middleware instance
auth_middleware = AuthMiddleware()

# Export dependencies
get_current_user = auth_middleware.get_current_user
get_current_active_user = auth_middleware.get_current_active_user
check_permissions = auth_middleware.check_permissions 