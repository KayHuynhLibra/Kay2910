"""
Bài tập 9: FastAPI

Mục tiêu:
- Hiểu cách tạo API với FastAPI
- Thực hành với Pydantic models
- Sử dụng dependency injection
"""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uvicorn

# TODO: Tạo FastAPI app
app = FastAPI(
    title="Todo API",
    description="API quản lý công việc",
    version="1.0.0"
)

# TODO: Pydantic models
class TodoBase(BaseModel):
    """
    Model cơ sở cho Todo
    """
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = False

class TodoCreate(TodoBase):
    """
    Model tạo Todo mới
    """
    pass

class Todo(TodoBase):
    """
    Model Todo đầy đủ
    """
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# TODO: In-memory database
todos = []
current_id = 1

# TODO: Dependency
def get_todo(todo_id: int):
    """
    Dependency để lấy todo theo id
    """
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo không tồn tại")

# TODO: API endpoints
@app.post("/todos/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    """
    Tạo todo mới
    """
    global current_id
    todo_dict = todo.model_dump()
    todo_dict["id"] = current_id
    todo_dict["created_at"] = datetime.now()
    todos.append(todo_dict)
    current_id += 1
    return todo_dict

@app.get("/todos/", response_model=List[Todo])
async def list_todos():
    """
    Lấy danh sách todos
    """
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo_by_id(todo: dict = Depends(get_todo)):
    """
    Lấy todo theo id
    """
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int,
    todo_update: TodoCreate,
    todo: dict = Depends(get_todo)
):
    """
    Cập nhật todo
    """
    todo_index = todos.index(todo)
    update_data = todo_update.model_dump()
    update_data["id"] = todo_id
    update_data["created_at"] = todo["created_at"]
    todos[todo_index] = update_data
    return update_data

@app.delete("/todos/{todo_id}")
async def delete_todo(todo: dict = Depends(get_todo)):
    """
    Xóa todo
    """
    todos.remove(todo)
    return {"message": "Todo đã được xóa"}

# TODO: Middleware
@app.middleware("http")
async def add_process_time_header(request, call_next):
    """
    Middleware thêm header thời gian xử lý
    """
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# TODO: Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Xử lý lỗi HTTP
    """
    return {
        "status_code": exc.status_code,
        "detail": exc.detail,
        "timestamp": datetime.now().isoformat()
    }

# TODO: Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
Bài tập về nhà:
1. Tạo một API quản lý người dùng với authentication
2. Tạo một API quản lý sản phẩm với phân trang
3. Tạo một API quản lý đơn hàng với validation
4. Tạo một API quản lý blog với categories
5. Tạo một API quản lý file với upload/download
""" 