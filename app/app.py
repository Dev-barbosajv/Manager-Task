from fastapi import FastAPI

from app.routers.task_router import router




app = FastAPI()

app.router.include_router(router, prefix="/api/v1")




if __name__ == "__main__":  
    import uvicorn  
  
    uvicorn.run(app, host="localhost", port=8000)