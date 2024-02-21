import os
import cv2

def deleteEmpty(root_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                image = cv2.imread(file_path)
                if image is None:
                    continue                 
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

                if len(faces) == 0:
                    os.remove(file_path)
    print("Boş resimler silindi")

# deleteEmpty("ExstraVeri/frame/Nasilsin")

def HepsiniSil(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png']
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension in image_extensions:
                os.remove(file_path)
                # print(f"{file_path} dosyası silindi.")

def countImages(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        image_count = 0
        for filename in filenames:
            if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                image_count += 1
    print(f"Klasör: {dirpath} - Toplam resim dosyası sayısı: {image_count}")

# countImages("ExstraVeri/frame/Merhaba")


