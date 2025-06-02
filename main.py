from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import Products


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home_page():
    return ("Acesse /docs")

@app.post("/product")
def new_product():
    return ("Cadastrar")