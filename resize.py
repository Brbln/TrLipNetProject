
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 00:21:51 2023

@author: Aslı Birbilen
"""
import cv2
from PIL import Image,ImageSequence
import os

# Hedef boyut
target_size = (256,256)
# Klasör yolu
path = "VeriSeti/Bir"
def resized_image(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".png") or filename.endswith(".jpg"):
                file_path = os.path.join(root, filename)
                image = Image.open(file_path)
                resized_image = image.resize(target_size)
                resized_image.save(file_path)
    print("Resized images!")
# resized_image(path)


def resized_gif(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".gif"):
                file_path = os.path.join(root, filename)
                gif_image = Image.open(file_path)
                frames = []
                for frame in ImageSequence.Iterator(gif_image):
                    resized_frame = frame.resize(target_size)
                    frames.append(resized_frame)

                gif_image.save(file_path, save_all=True, append_images=frames)

    print("Resized GIF images!")

# resized_gif(path)


