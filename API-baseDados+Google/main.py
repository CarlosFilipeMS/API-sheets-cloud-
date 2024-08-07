from fastapi import FastAPI
import auth, functions

app = FastAPI()

app.include_router(auth.router)
app.include_router(functions.router)