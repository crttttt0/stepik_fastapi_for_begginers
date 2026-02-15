from fastapi import FastAPI, Depends


class Paginator:
    def __init__(self, limit: int = 10, page: int = 1):
        self.limit = limit
        self.page = page


app = FastAPI()


@app.get("/users")
async def all_users(pagination: Paginator = Depends(Paginator)):
    return {"user": pagination}
