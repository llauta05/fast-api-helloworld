from pydoc import describe
from turtle import title
from typing import Optional
from unittest.util import _MAX_LENGTH
from pydantic import BaseModel
from fastapi import FastAPI, Body, Query, Path


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
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="this is the persona name"
        ),
    age: Optional[int] = Query(
        ...,
        title="Person age",
        description="this is the person age"
        )
):
    return {name: age}
 
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="identity person id",
        description="this is id the person"
        )
):
    return {person_id: "existe"}














