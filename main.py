from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # create instance of FastAPI

class Custom(BaseModel):
    name: str
    age: int

# The app instance is the main omponent of FastApI application. It is used to configure the application.

# /ping is path of the end point.

# @app.get() is a decorator is used to define an endpoint. 
@app.get('/ping')
async def root():
    return {'message': 'Hello World'}

# In FastAPI, serialization is the process of converting Python objects (like Pydantic models) into JSON-compatible data types to send as HTTP responses.
# This is usually handled automatically by FastAPI using Pydantic.
# Here {'message': 'Hello World'} is python Dictionary but it is converted into json.

# @app.get('/blogs/{blog_id}')
# async def read_blog(blog_id : int):
#     return {"blog_id": blog_id}

# @app.get('/blogs/comments') 
# async def read_comment():
#     return {"comment": "No comment"}
# The error occurs because /blogs/comments matches the path /blogs/{blog_id} first, trying to parse "comments" as an integer.

@app.get('/blogs/comments')
async def read_comment():
    return {"comment": "No comment"}

# query params q
@app.get('/blogs/{blog_id}')
async def read_blog(blog_id : int, q: str = None):
    print(q)
    return {"blog_id": blog_id}

# in body raw section give {
#     "name": "Aryan Kashyap",
#     "age": 21
# } and in header section give Content-Type: application/json
@app.post('/blogs/{blog_id}')
async def create_blog(blog_id : int, request_body: Custom, q: str = None):
    print(request_body)
    print(q)
    return {"blog_id": blog_id}