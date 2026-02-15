from fastapi import FastAPI, Query, Depends, HTTPException, status
from typing import Annotated

app = FastAPI()


async def pagination_path_func(page: int):
    if page < 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Page does not exist"
        )
    elif page == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid page value"
        )


async def pagination_func(limit: int = Query(10, gt=0), page: int = 1) -> dict:
    return {"limit": limit, "page": page}


@app.get("/messages", dependencies=[Depends(pagination_path_func)])
async def get_all_messages(pagination: dict = Depends(pagination_func)) -> dict:
    return {"messages": pagination}
