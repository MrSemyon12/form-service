from tinydb import TinyDB
import uvicorn
from fastapi import FastAPI, Body, HTTPException, status

from utils import parse_form_data, get_marked_form, find_matching_template

app = FastAPI()

db = TinyDB("db.json")


@app.post("/get_form")
def get_form(form_data: str = Body()):
    try:
        form_fields = parse_form_data(form_data)
        marked_form = get_marked_form(form_fields)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Ошибка при разборе данных формы",
        )

    matching_template = find_matching_template(db.all(), marked_form)

    return matching_template if matching_template else marked_form


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
