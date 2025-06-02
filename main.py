from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import Products


Base.metadata.create_all(bind=engine)

app = FastAPI()

class ProductsSchema(BaseModel):
    name: str
    description: str
    qnt_products: int
    price: float
    image: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home_page():
    return ("Acesse /docs")

@app.post("/product")
def new_product(product: ProductsSchema, db: Session = Depends(get_db)):
    product = Products(name=product.name,
                        description=product.description,
                        qnt_products=product.qnt_product,
                        price=product.price,
                        image=product.image)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
