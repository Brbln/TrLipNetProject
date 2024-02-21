import cv2
import numpy as np
from PIL import Image, ImageSequence
import os


def gif_kirp1(gif_path, hedef_klasor):
    # Zoom değerleri
    zoom_x = 25
    zoom_y = 150
    zoom_w = 200
    zoom_h = 200

    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)

    gif_image = Image.open(gif_path)
    frames = []
    for frame in ImageSequence.Iterator(gif_image):
        frame_cv = np.array(frame.convert("RGBA"))
        zoomed_frame = frame_cv[zoom_y:zoom_y + zoom_h, zoom_x:zoom_x + zoom_w]
        resized_frame = cv2.resize(zoomed_frame, (256, 256))
        frames.append(Image.fromarray(resized_frame))

    file = os.path.basename(gif_path)
    new_file = file  # Dosya adını değiştirmeden al
    new_file_path = os.path.join(hedef_klasor, new_file)
    frames[0].save(new_file_path, save_all=True, append_images=frames[1:], loop=0,
                   duration=gif_image.info['duration'])

    print(f"{file} isimli GIF görüntüsü zoom yapıldı ve kaydedildi: {new_file_path}")

    return new_file_path  # Düzenlenmiş dosyanın yolunu geri döndürelim


def kirp_klasor(kaynak_klasor, hedef_klasor):
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)
    dosya_listesi = os.listdir(kaynak_klasor)
    for dosya_adi in dosya_listesi:
        dosya_yolu = os.path.join(kaynak_klasor, dosya_adi)
        if dosya_adi.lower().endswith('.gif'):
            new_file_path = gif_kirp1(dosya_yolu, hedef_klasor)

            # Dosyayı adını değiştirdiğimiz yeni dosya adıyla kaydet
            os.rename(new_file_path, dosya_yolu)

    print("İşlem tamamlandı.")


# kaynak_klasor = "C:/Users/abrbl/VeriSeti/_veri/sonGif/Gel/video17528346663 - Kopya.gif"
# hedef="C:/Users/abrbl/VeriSeti/_veri/sonGif/Gel"
#hedef_klasor = "C:/Users/abrbl/VeriSeti/_veri/sonGif/RenkliGif/Gel"
#kirp_klasor(kaynak_klasor, hedef_klasor)
# gif_kirp1(kaynak_klasor,hedef)