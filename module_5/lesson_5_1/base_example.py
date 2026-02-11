from fastapi import FastAPI, Depends, Query, status


app = FastAPI(title=" FastAPI Dependency Injection (DI)")


async def pagination_func(limit: int = Query(10, ge=0), page: int = 1) -> list:
    return [{"limit": limit, "page": page}]


@app.get("/messages", status_code=status.HTTP_200_OK)
async def get_all_messages(pagination: list = Depends(pagination_func)) -> dict:
    return {"messages": pagination}


@app.get("/comments", status_code=status.HTTP_200_OK)
async def get_all_comments(pagination: list = Depends(pagination_func)) -> dict:
    return {"comments": pagination}