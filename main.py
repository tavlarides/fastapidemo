from enum import StrEnum
from fastapi import FastAPI

app = FastAPI()

ModelName = StrEnum('ModelName', ["alexnet", "resnet", "lenet"])

@app.get("/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}