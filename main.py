from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def hello(request: Request):
    return templates.TemplateResponse(
        "base.html", {"request": request, "title": "Jinja and FastAPI"}
    )


@app.get("/form")
async def form(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "name": "Lola",
            "fields": [
                {"name": "field1", "label": "Field 1", "type": "text"},
                {"name": "field2", "label": "Field 2", "type": "text"},
                {"name": "lola", "label": "Lola", "type": "text"},
                # Add more fields as needed
            ],
        },
    )


@app.post("/submit")
async def handleForm(name: str=Form(...), fields: list[str]=Form(...)):
    # form_data = await request.form()
    print(f"Name: {name}")

    # for field in fields:
    #     print(f"Field: {field}")

    return {"message": "Data submitted successfully"}