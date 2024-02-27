from fastapi import APIRouter, status, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from users import schemas
from typing import Annotated
from app.types import DBConnectionDep
from users.controllers import AuthController
from users.auth import auth

security = HTTPBearer()

auth_router = APIRouter(prefix="/auth", tags=['auth'])

AuthControllerDep = Annotated[AuthController, Depends(AuthController)]

@auth_router.post("/singup", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
async def singup(controller: AuthControllerDep, db: DBConnectionDep, body: schemas.UserCreationModel):
    exist_user = await controller.get_user(email=body.email, db=db)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User already exist')
    body.password = auth.password.hash(body.password)
    return await controller.create(body, db)

@auth_router.post('/login', response_model=schemas.TokenModel)
async def login(db: DBConnectionDep, body: OAuth2PasswordRequestForm = Depends()):
    return await auth.authenticate(body, db)

@auth_router.get('/refresh_token', response_model=schemas.TokenModel)
async def refresh_token(db: DBConnectionDep, credentials: HTTPAuthorizationCredentials = Security(security)):
    return await auth.refresh(credentials.credentials, db)