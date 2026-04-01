from fastapi import UploadFile, File

def predict_image(file_bytes):
    return "OK_TEST"

from fastapi import APIRouter

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        
        # просто тест
        result = predict_image(contents)

        return {"result": result}

    except Exception as e:
        return {"error": str(e)}
