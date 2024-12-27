from fastapi import FastAPI
from routers.user import user_router
from routers.book import book_router
from routers.borrow import borrow_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["Users"])
# app.include_router(book_router, prefix="/book", tags=["Books"])
# app.include_router(borrow_router, prefix="/borrow", tags=["Borrow"])

@app.get("/")
def home():
    return {"Message": "Welcome home"}