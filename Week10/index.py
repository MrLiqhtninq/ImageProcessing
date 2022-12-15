import os
import time
import cv2 
import pafy
import numpy as np
from rich.console import Console
from rich.theme import Theme 
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)

def Week10(index):
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        img = cv2.imread('/Users/mrliqhtninq/Desktop/ImageProcessing/images/carpet.jpeg')
        kernel = np.ones((5, 5), np.uint8)
        if index=="1":
            erosion = cv2.erode(img, kernel,iterations=1)
            cv2.imshow("Original Image", img)
            cv2.imshow("Erosion Image", erosion)
            cv2.waitKey(0)
        elif index=="2":
            dilation = cv2.dilate(img, kernel,iterations=1)
            cv2.imshow("Original Image", img)
            cv2.imshow("Dilation Image", dilation)
            cv2.waitKey(0)
        elif index=="3":
            opening = cv2.morphologyEx(img.astype(np.float32),cv2.MORPH_OPEN,kernel)
            cv2.imshow("Original Image", img)
            cv2.imshow("Opening Image", opening)
            cv2.waitKey(0)
        elif index=="4":   
            closing = cv2.morphologyEx(img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
            cv2.imshow("Original Image", img)
            cv2.imshow("Closing Image", closing)
            cv2.waitKey(0)
        else:
            console.print("Böyle bir ödev mevcut değil",style="error")
       
        
        
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")