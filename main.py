from pydoc import describe
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from pydantic import Field
from fastapi import FastAPI, Body, Query, Path


app = FastAPI()

class HairColor(Enum):
    white= "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"

class Location(BaseModel):
    city: str
    country: str
    state: str


class Person(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=115)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {"hello": "world"}


# request and response body
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


@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="person id",
        description="this is the person id",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    result = person.dict()
    result.update(location.dict())
    return result
