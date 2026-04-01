from fastapi import UploadFile, File
from fastapi import APIRouter

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    
    return {"class": "test_ok"}
