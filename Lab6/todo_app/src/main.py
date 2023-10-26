from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

@app.get("/api")
def first_api():
    return {"msg": "Hello World"}

@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return {"msg": path_param}

@app.get("/books/")
def first_apiV3(title: str):
    return {"msg": title}

@app.get("/books/{book_id}/")
def first_apiV4(book_id: int, title: str):
    return {"msg": book_id, "title": title}

@app.post("/books/create_book")
def first_apiV5(new_book=Body()):
    print(new_book)
    return {"msg": new_book}

class Book(BaseModel):
    title: str
    author: str
    category: str

books_db = {
    1: {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "category": "Fantasy"
    },
    
    2: {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "category": "Fantasy"
    },
    
    3: {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "category": "Romance"
    }
}

@app.put("/books/{book_id}")
def first_apiV6(book_id: int, book: Book):
    books_db[book_id] = book.model_dump()
    return books_db[book_id]

@app.delete("/books/{book_id}")
def first_apiV7(book_id: int):
    books_db.pop(book_id)
    return {"msg": "Deleted"}