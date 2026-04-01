import torch
from torchvision import transforms
from model import get_model
from utils import detect_face

classes = ["asian", "black", "indian", "white", "others"]

model = get_model(5)

# ВРЕМЕННО БЕЗ model.pth (чтобы не было ошибки)
model.eval()

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict(image_path):
    face = detect_face(image_path)

    if face is None:
        return "No face detected"

    face = transform(face).unsqueeze(0)

    with torch.no_grad():
        output = model(face)
        _, pred = torch.max(output, 1)

    return classes[pred.item()]
