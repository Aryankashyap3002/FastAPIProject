from fastapi import FastAPI, Depends 
from pydantic import BaseModel
from typing import Optional, List
from models import TodoModel
from database import Sessionlocal, engine
from sqlalchemy.orm import Session

app = FastAPI() # create instance of FastAPI


TodoModel.metadata.create_all(bind=engine) # Create the table in the database

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int
    
    class Config:
        orm_mode = True
        
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
    

@app.get('/todos', response_model=List[TodoResponse])
async def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

# @app.get('/todos/{todo_id}')
# async def get_todo(todo_id: int):
#     for todo in todos:
#         if todo['id'] == todo_id:
#             return todo
#     return {"error": "No Todo found"}

# @app.post('/todos')
# async def create_todo(todo: TodoModel):
#     todos.append(todo.dict()) # Append the todo to the list
#     return todos[-1] # Return the last todo

# @app.delete('/todos/{todo_id}')
# async def delete_todo(todo_id: int):
#     for todo in todos:
#         if todo['id'] == todo_id:
#             todos.remove(todo)
#             return {"message": "Deleted Todo successfully"}
#     return {"error": "Todo not found"}

# @app.put('/todos/{todo_id}')
# async def update_todo(todo_id: int, newTodo: Todo):
#     for index, todo in enumerate(todos):
#         if todo['id'] == todo_id:
#             todos[index] = newTodo.dict()
#             return {"message": "Todo updated successfully", "todo": todos[index]}
#     return {"error": "Todo not found"}
