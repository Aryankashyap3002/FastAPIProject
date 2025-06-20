from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI() # create instance of FastAPI

todos = [] # Create a empty list to store todos, in memory db

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get('/todos')
async def get_todos():
    return todos

@app.get('/todos/{todo_id}')
async def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return {"error": "No Todo found"}

@app.post('/todos')
async def create_todo(todo: Todo):
    todos.append(todo.dict()) # Append the todo to the list
    return todos[-1] # Return the last todo

@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return {"message": "Deleted Todo successfully"}
    return {"error": "Todo not found"}

@app.put('/todos/{todo_id}')
async def update_todo(todo_id: int, newTodo: Todo):
    for index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            todos[index] = newTodo.dict()
            return {"message": "Todo updated successfully", "todo": todos[index]}
    return {"error": "Todo not found"}
