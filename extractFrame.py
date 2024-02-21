import cv2
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import FrameDelete as sil
import resize
import gif2 as gif
import GifKirp as kirp


def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frames.append(frame)            
            count += 1
        else:
            break
    cap.release()   
    return frames

#extract_frames("Görüşürüz/video2980391566.mp4")

def detect_faces(frames):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face_frames = []
    num_frames = min(len(frames), 50)
    for frame_idx, frame in enumerate(frames[-(num_frames+2):-2]):
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=4)
        for (x, y, w, h) in faces:
            face_frame = frame[y:y+h, x:x+w]
            face_frames.append(face_frame)   
    return face_frames   

#detect_faces(extract_frames("OzurDilerim/video13215206451.mp4"))


def save_faces(face_frames, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for i, frame in enumerate(face_frames):
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #resimleri griye çevirir 
        cv2.imwrite(os.path.join(output_path, f"{i:04}.jpg"), frame)  
        
#save_faces(detect_faces(extract_frames("OzurDilerim/video3917294517.mp4")),"OzurDilerim/Frames/video2")

def e_Video_Frames(videoPath,savePath):
    frames = extract_frames(videoPath)
    face_frames = detect_faces(frames)
    save_faces(face_frames,savePath)    
    print(f"Extracted {len(face_frames)} faces from {videoPath}")
     
def e_Folder_Frames(folder_path, output_folder):
    video_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".mp4")]) 
    for video_file in video_files:
        video_path = os.path.join(folder_path, video_file).replace("\\","/")
        output_path = os.path.join(output_folder, video_file[:-4]).replace("\\","/")
        e_Video_Frames(video_path, output_path)
        print("videolar: "+video_path)

        
#klasoru gif dosyalarına çevirme
# fpath="ExstraVeri/Evet"
# opath="ExstraVeri/frame/Nasilsin"
# hedef="ExstraVeri/frame/Gorusuruz_dudak"
# kayit="ExstraVeri/gif/Evet"
# e_Folder_Frames(fpath, opath)
# sil.deleteEmpty(opath)
# sil.countImages(opath)
# resize.resized_image(opath)
# gif.dosyaGif(opath, kayit)
# kirp.kirp_klasor(kayit, kayit)


#video gife çevirme
# path="_Test/Deneme/gel.mp4"
# klasor="_Test/Deneme"
# save="_Test/Deneme/gel.gif"
# # e_Video_Frames(path,klasor)
# # sil.deleteEmpty(klasor)
# # resize.resized_image(klasor)
# # gif.videoGif(klasor,save) 
# kirp.gif_kirp1(save, klasor)
# video_files = sorted([f for f in os.listdir(klasor) if f.endswith(".gif")]) 
# for video_file in video_files:
#     sil.HepsiniSil(klasor)

