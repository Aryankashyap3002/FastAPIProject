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

@app.get('/todos/{todo_id}', response_model=TodoResponse)
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    return todo

# Content-Type: application/json add this on header
@app.post('/todos', response_model=TodoResponse)
async def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    new_todo = TodoModel(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@app.delete('/todos/{todo_id}', response_model=TodoResponse)
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return todo

@app.put('/todos/{todo_id}', response_model=TodoResponse)
async def update_todo(todo_id: int, updated_todo: TodoBase, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        return {"error": "Todo not found"}

    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.completed = updated_todo.completed

    db.commit()
    db.refresh(todo)
    return todo

