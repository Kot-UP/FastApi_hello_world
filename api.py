from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI(title="My_First_Project",
              summary="My CRUD application.",
              description="""The CRUD application supports writing, reading, updating and deleting posts.""",
              version="0.0.1",
              openapi_url="/api/v1/openapi.json"
    # docs_url=None,  отключить Swagger UI
    # redoc_url=None  отключить Redoc
)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


# @app.get("/user")
# async def search(people: Annotated[list[str], Query()]) -> dict:
#     return {"user": people}


@app.get("/user/{username}")
async def login(username: Annotated[str, Path(min_length=3, max_length=15, description="Enter your username", example="Shasha")],
                first_name: Annotated[str | None, Query(max_length=10, regex="^J|s$")] = None) -> dict:
    return {"user": username, "Name": first_name}


@app.get("/hello/{first_name}/{last_name}")
async def welcome_user(first_name: str, last_name: str) -> dict:
    return {"user": f'Hello {first_name} {last_name}'}


@app.get("/order/{order_id}")
async def order(order_id: int) -> dict:
    return {"id": order_id}


@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {"Employee": name, "Company": company, "Department": department}