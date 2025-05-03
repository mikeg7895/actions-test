from fastapi import FastAPI, status, Response
import random

app = FastAPI()

@app.get("/")
async def index(response: Response):
    number = random.randint(1, 2)
    if number == 1:
        response.status_code = status.HTTP_200_OK
        return {"message": "Hello, World!"}
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Goodbye, World!"}
