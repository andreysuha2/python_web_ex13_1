from fastapi import FastAPI
from contacts.routes import router as contacts_router 
from users.routes import auth_router
from app.settings import BASE_URL_PREFIX, APP_HOST, APP_PORT
import uvicorn

app = FastAPI()

routers = [auth_router, contacts_router]

[app.include_router(router, prefix=BASE_URL_PREFIX) for router in routers]

@app.get('/')
def read_root():
    return {"message": "Contact app!"}
    
    
if __name__ == "__main__":
    uvicorn.run("app.main:app", host=APP_HOST, port=APP_PORT, reload=True)