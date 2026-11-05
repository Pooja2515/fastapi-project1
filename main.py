
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from data import products

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return {"message": "Welcome to Product Management"}

@app.get("/products")
def get_products(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="products.html",
        context={
            "products": products,
        }
    )
