import cv2

# Загружаем модель для обнаружения лиц
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_face(image_path):
    # Читаем изображение
    img = cv2.imread(image_path)

    # Переводим в чёрно-белое (нужно для детектора)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ищем лица
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Если лицо не найдено
    if len(faces) == 0:
        return None

    # Берём первое найденное лицо
    x, y, w, h = faces[0]

    # Вырезаем лицо
    face = img[y:y+h, x:x+w]

    return face
