"""ui api main"""
from fastapi import FastAPI
import uvicorn

from routers import router as ui_router
from shared.config import FASTAPI_HOST, FASTAPI_PORT

app = FastAPI()
app.include_router(ui_router)

def main():
    """run ui api"""
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)
    
    
if __name__ == '__main__':
    main()