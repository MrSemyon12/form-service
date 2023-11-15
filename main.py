from tinydb import TinyDB
import uvicorn
from fastapi import FastAPI, Body

from utils import parse_form_data, get_marked_form, find_matching_template

app = FastAPI()

db = TinyDB("db.json")


@app.post("/get_form")
def get_form(form_data: str = Body()):
    form_fields = parse_form_data(form_data)
    marked_form = get_marked_form(form_fields)
    matching_template = find_matching_template(db.all(), marked_form)

    return matching_template if matching_template else marked_form


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
