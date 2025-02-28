from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
def welcome():
    return "Anonymous"


@app.get("/welcome/{name}")
def welcome_name(name: Optional[str]):
    return f"Selamat datang {name}"
