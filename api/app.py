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

    result = "WORKING OK"

    return {"prediction": result}
import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
