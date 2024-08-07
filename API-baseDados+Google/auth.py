from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi import APIRouter, Depends

# Criando o modelo de login 
class LoginCredentials(BaseModel):
    username: str
    password: str

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# OBS: Em um ambiente de produção essa chave não deve ficar armazenada no código 
SECRET_KEY = "a2f161ef7c22c58014a6cb2aef1a6fad2bb97d6cc6b51634707ff989358bdcb3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

# Definindo o usuário autenticado -> o "username" e a "password", serão passados no body da requisição de auth
def authenticate_user(username: str, password: str) -> Optional[dict]:
    if username == "definindo_username@user.admin" and password == "FiaXGyM1A213u@fW":
        return {"username": username}
    return None

# Criando o token para acesso -> esse token será passado no header da próxima requisição
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"username": username}

# Incluindo uma rota para receber um token de acesso e verificando a validade do token
@router.post("/api/auth/token")
async def login_for_access_token(credentials: LoginCredentials):
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}