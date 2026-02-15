from fastapi import FastAPI, Depends
from fastapi.requests import Request

app = FastAPI()


async def sub_dependency(request: Request) -> str:
    print("Саб зависимость")
    return request.method


async def main_dependency(method: str = Depends(sub_dependency)) -> str:
    print("Мейн зависимость")
    return method


@app.get("/method", response_model=str)
async def get_method(method=Depends(main_dependency)) -> str:
    print("Роут")
    return method
