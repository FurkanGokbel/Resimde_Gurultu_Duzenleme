# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan Gökbel
# @File : Erosion_Dilation_Opening_Closing.py
# @Software: PyCharm

import numpy as np
import cv2

kamera = cv2.VideoCapture(0)  # Dahili Kamera çağırılıyor

while (1):
    ret, frame = kamera.read()
    # Renk filitrelemede HSV uzayında calısmak daha kolaylık sağlayacaktır.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dusuk_beyaz = np.array([0, 0,
                            140])  # girilen renk icin alt üst renk aralığı tanımlanıp sadece o renk değerini geçirme işlemi yapılıyor
    ust_beyaz = np.array([256, 60, 256])

    mask = cv2.inRange(hsv, dusuk_beyaz, ust_beyaz)
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)  # Filitrelemede istenmeyen gürültüleri tam olarak siliyoruz
    dilation = cv2.dilate(mask, kernel, iterations=1)  # Gürültüyü ön plana cıkarıyor

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    cv2.imshow('orjinal', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son', son_resim)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
