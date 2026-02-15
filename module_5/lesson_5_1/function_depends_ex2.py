from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Annotated

app = FastAPI(title="Messages CRUD DI")


class Post(BaseModel):
    id: int
    text: str


class CreatePost(BaseModel):
    text: str


db: list[Post] = [
    Post(id=1, text="у тебя дома есть газовая плита"),
    Post(id=2, text="угарный газ пахнет шоколадом"),
    Post(id=3, text="ртуть в 5 раз слаще сахара"),
    Post(id=4, text="ты это выложил если что"),
    Post(id=5, text="отрежь хуй папры и покажи маме пусть идет нахуй"),
]


def get_next_id() -> int:
    return max((post.id for post in db), default=1)


async def get_post_or_404(id: int) -> Post:
    for post in db:
        if post.id == id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


async def get_post_index_or_404(id: int) -> int:
    for i, post in enumerate(db):
        if post.id == id:
            return i
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


type PostOrNotFound = Annotated[Post, Depends(get_post_or_404)]
type PostIndexOrNotFound = Annotated[Post, Depends(get_post_index_or_404)]


@app.get("/message/{id}", response_model=Post, status_code=status.HTTP_200_OK)
async def get_message(post: PostIndexOrNotFound) -> Post:
    return post


@app.post("/message", status_code=status.HTTP_201_CREATED)
async def create_message(post: CreatePost) -> str:
    new_post = Post(id=get_next_id(), text=post.text)
    db.append(new_post)

    return "Message created"


@app.put("/message/{id}", response_model=Post, status_code=status.HTTP_200_OK)
async def update_message(post: PostOrNotFound, new_post: CreatePost):
    post = new_post
    return post


@app.delete("/message/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(post_id: PostIndexOrNotFound) -> None:
    del db[post_id]
