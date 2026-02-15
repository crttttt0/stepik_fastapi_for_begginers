from fastapi import FastAPI, Depends
from fastapi.requests import Request

log_user = []


async def log_client(request: Request) -> None:
    log_user.append(request.headers)


app = FastAPI(dependencies=[Depends(log_client)])


@app.get("/log_user")
async def print_log_user() -> dict:
    return {"users": log_user}
