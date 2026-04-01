from fastapi import FastAPI, File, UploadFile
import shutil
from predict import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API работает 🚀"}

@app.post("/predict/")
async def predict_api(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict(file_path)

    return {"prediction": result}
