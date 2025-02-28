from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
def welcome():
    return "Anonymous"


@app.get("/welcome/{name}")
def welcome_name(name: str):
    return f"Selamat datang {name}"
