from src.main import first_api, first_apiV2, first_apiV3, first_apiV4, first_apiV5, first_apiV6, first_apiV7
from src.main import Book

def test_first_api():
    response = first_api()
    assert response == {"msg": "Hello World"}

def test_first_apiV2():
    response = first_apiV2("test_param")
    assert response == {"msg": "test_param"}

def test_first_apiV3():
    response = first_apiV3("test_title")
    assert response == {"msg": "test_title"}

def test_first_apiV4():
    response = first_apiV4(42, "test_title")
    assert response == {"msg": 42, "title": "test_title"}

def test_first_apiV5():
    new_book = {"title": "New Book", "author": "Author", "category": "Fiction"}
    response = first_apiV5(new_book)
    assert response == {"msg": new_book}

def test_first_apiV6():
    updated_book = {"title": "Updated Book", "author": "Updated Author", "category": "Updated Category"}
    response = first_apiV6(1, Book(**updated_book))
    assert response == updated_book

def test_first_apiV7():
    response = first_apiV7(1)
    assert response == {"msg": "Deleted"}