"""app main"""
from fastapi import FastAPI
import uvicorn

from routers import router as auth_router

from shared.models import User
from shared.database import engine
from shared.config import FASTAPI_HOST, FASTAPI_PORT

User.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)

def main():
    """run auth api"""
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)

if __name__ == '__main__':
    main()
