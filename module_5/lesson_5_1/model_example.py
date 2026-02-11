from fastapi import FastAPI, Depends, Query, HTTPException, status
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    id: int
    text: str


db: list[Post] = []