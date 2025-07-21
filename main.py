from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from fastapi.middleware.cors import CORSMiddleware
from models import Products


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

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
                        qnt_products=product.qnt_products,
                        price=product.price,
                        image=product.image)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Products).all()

@app.get("/{product_id}/product")
def get_product_by_id(product_id: int,
                       db: Session = Depends(get_db)):
    return db.query(Products).filter(product_id == Products.id).first()

@app.put("/update/product")
def update_product(id: int, user: ProductsSchema,
                   db: Session = Depends(get_db)):
    existing_user = db.query(Products).filter(id == Products.id).first()
    for key, value in user.dict().items():
        setattr(existing_user, key, value)
    db.commit()
    db.refresh(existing_user)
    return existing_user

@app.delete("/{id}/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    delete = db.query(Products).filter(id == Products.id).first()
    db.delete(delete)
    db.commit()
    return {"message:" f"User with ID {id} was deleted succssessfully"}




