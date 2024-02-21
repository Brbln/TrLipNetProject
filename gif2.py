from PIL import Image
import os

def videoGif(klasor, kayit):
    dosyalar = os.listdir(klasor)
    dosya_adi = os.path.join(klasor, os.path.basename(kayit))
    fotograflar = [f for f in dosyalar if f.endswith(('.jpg', '.jpeg', '.png'))]
    fotograflar.sort()
    ilk_fotograf = Image.open(os.path.join(klasor, fotograflar[0]))
    genislik, yukseklik = ilk_fotograf.size

    gif = Image.new('RGBA', (genislik, yukseklik))
    frame_listesi = []
    for fotograf in fotograflar:

        fotograf_yolu = os.path.join(klasor, fotograf)
        frame = Image.open(fotograf_yolu)
        frame_listesi.append(frame.copy())
        gif.paste(frame, (0, 0))
    gif.save(kayit, format='GIF', append_images=frame_listesi[1:], save_all=True, duration=100, loop=0)
    print(f"{dosya_adi} oluşturuldu")

def dosyaGif(klasor,kayit):
    if not os.path.exists(kayit):
        os.makedirs(kayit)
        videoGif(klasor,kayit)
    for root, dirs, files in os.walk(klasor):
        for alt_klasor in dirs:
            alt_klasor_yolu = os.path.join(root, alt_klasor).replace("\\","/")
            gif_dosya_adi = alt_klasor + '.gif'
            gif_kayit_yolu = os.path.join(kayit, gif_dosya_adi).replace("\\","/")
            videoGif(alt_klasor_yolu, gif_kayit_yolu)
            print(f"{alt_klasor} klasöründeki fotoğraflar GIF olarak oluşturuldu.")
            
# klasor = "C:/Users/abrbl/VeriSeti/_veri/frame/Merhaba"
# kayit = "C:/Users/abrbl/VeriSeti/_veri/sonGif/Merhaba"
# dosyaGif(klas"or, kayit)
