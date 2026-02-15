from fastapi import FastAPI, Depends


class Paginator:
    def __init__(self, limit: int, page: int):
        self.limit = limit
        self.page = page

    def __call__(self, limit: int = 10, page: int = 1):
        if limit < self.limit:
            return {"limit": self.limit, "page": page}
        else:
            return {"limit": limit, "page": page}


app = FastAPI()


@app.get("/users")
async def all_users(pagination: list = Depends(Paginator(10, 5))):
    return {"user": pagination}
