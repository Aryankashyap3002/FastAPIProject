from fastapi import FastAPI


app = FastAPI() # create instance of FastAPI

# The app instance is the main omponent of FastApI application. It is used to configure the application.

# /ping is path of the end point.

@app.get('/ping')
async def root():
    return {'message': 'Hello World'}


