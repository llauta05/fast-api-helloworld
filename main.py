from typing import Optional
from unittest.util import _MAX_LENGTH
from pydantic import BaseModel
from fastapi import FastAPI, Body, Query


app = FastAPI()

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"hello": "world"}


#request and response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: Optional[int] = Query(...)
):
    return {name: age}
 