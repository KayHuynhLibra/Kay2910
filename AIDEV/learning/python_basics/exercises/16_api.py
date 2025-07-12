"""
Bài tập 16: API

Mục tiêu:
- Hiểu cách tạo REST API
- Thực hành với FastAPI
- Sử dụng Pydantic models
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uvicorn

# TODO: Pydantic models
class UserBase(BaseModel):
    """
    Base user model
    """
    email: EmailStr
    username: str

class UserCreate(UserBase):
    """
    User creation model
    """
    password: str

class UserUpdate(BaseModel):
    """
    User update model
    """
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    """
    User response model
    """
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    """
    Base post model
    """
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    """
    Post creation model
    """
    pass

class PostUpdate(BaseModel):
    """
    Post update model
    """
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class Post(PostBase):
    """
    Post response model
    """
    id: int
    created_at: datetime
    updated_at: datetime
    author_id: int
    
    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    """
    Base comment model
    """
    content: str

class CommentCreate(CommentBase):
    """
    Comment creation model
    """
    pass

class CommentUpdate(BaseModel):
    """
    Comment update model
    """
    content: Optional[str] = None

class Comment(CommentBase):
    """
    Comment response model
    """
    id: int
    created_at: datetime
    updated_at: datetime
    author_id: int
    post_id: int
    
    class Config:
        orm_mode = True

# TODO: FastAPI app
app = FastAPI(
    title="Blog API",
    description="A simple blog API",
    version="1.0.0"
)

# TODO: Dependencies
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Get current user from token
    """
    # TODO: Implement token validation
    return {"username": "testuser"}

# TODO: API routes
@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    """
    Create new user
    """
    # TODO: Implement user creation
    return {
        "id": 1,
        "email": user.email,
        "username": user.username,
        "is_active": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

@app.get("/users/", response_model=List[User])
async def get_users(skip: int = 0, limit: int = 10):
    """
    Get all users
    """
    # TODO: Implement user listing
    return []

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """
    Get user by ID
    """
    # TODO: Implement user retrieval
    return {
        "id": user_id,
        "email": "test@example.com",
        "username": "testuser",
        "is_active": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate, current_user: dict = Depends(get_current_user)):
    """
    Update user
    """
    # TODO: Implement user update
    return {
        "id": user_id,
        "email": user.email or "test@example.com",
        "username": user.username or "testuser",
        "is_active": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, current_user: dict = Depends(get_current_user)):
    """
    Delete user
    """
    # TODO: Implement user deletion
    return {"message": "User deleted"}

@app.post("/posts/", response_model=Post)
async def create_post(post: PostCreate, current_user: dict = Depends(get_current_user)):
    """
    Create new post
    """
    # TODO: Implement post creation
    return {
        "id": 1,
        "title": post.title,
        "content": post.content,
        "published": post.published,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "author_id": 1
    }

@app.get("/posts/", response_model=List[Post])
async def get_posts(skip: int = 0, limit: int = 10):
    """
    Get all posts
    """
    # TODO: Implement post listing
    return []

@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: int):
    """
    Get post by ID
    """
    # TODO: Implement post retrieval
    return {
        "id": post_id,
        "title": "Test Post",
        "content": "Test Content",
        "published": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "author_id": 1
    }

@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post: PostUpdate, current_user: dict = Depends(get_current_user)):
    """
    Update post
    """
    # TODO: Implement post update
    return {
        "id": post_id,
        "title": post.title or "Test Post",
        "content": post.content or "Test Content",
        "published": post.published or True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "author_id": 1
    }

@app.delete("/posts/{post_id}")
async def delete_post(post_id: int, current_user: dict = Depends(get_current_user)):
    """
    Delete post
    """
    # TODO: Implement post deletion
    return {"message": "Post deleted"}

@app.post("/posts/{post_id}/comments/", response_model=Comment)
async def create_comment(post_id: int, comment: CommentCreate, current_user: dict = Depends(get_current_user)):
    """
    Create new comment
    """
    # TODO: Implement comment creation
    return {
        "id": 1,
        "content": comment.content,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "author_id": 1,
        "post_id": post_id
    }

@app.get("/posts/{post_id}/comments/", response_model=List[Comment])
async def get_comments(post_id: int, skip: int = 0, limit: int = 10):
    """
    Get all comments for a post
    """
    # TODO: Implement comment listing
    return []

@app.put("/comments/{comment_id}", response_model=Comment)
async def update_comment(comment_id: int, comment: CommentUpdate, current_user: dict = Depends(get_current_user)):
    """
    Update comment
    """
    # TODO: Implement comment update
    return {
        "id": comment_id,
        "content": comment.content or "Test Comment",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "author_id": 1,
        "post_id": 1
    }

@app.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int, current_user: dict = Depends(get_current_user)):
    """
    Delete comment
    """
    # TODO: Implement comment deletion
    return {"message": "Comment deleted"}

# TODO: Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
Bài tập về nhà:
1. Tạo một REST API cho một ứng dụng blog
2. Tạo một REST API cho một ứng dụng e-commerce
3. Tạo một REST API cho một ứng dụng social media
4. Tạo một REST API cho một ứng dụng task management
5. Tạo một REST API cho một ứng dụng file sharing
""" 