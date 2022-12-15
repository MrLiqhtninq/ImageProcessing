import os
import time
import cv2 
import pafy
import numpy as np
from rich.console import Console
from rich.theme import Theme 
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)

def Week9(index):
    console.print("Çıkmak için CTRL+C",style="error")
    try:
       #HSI RGB 
        img = cv2.imread('/Users/mrliqhtninq/Desktop/ImageProcessing/images/lake.jpeg')
        if index=="1":
            rgb = cv2.cvtColor(img, cv2.COLOR_HSV2RGB_FULL)
            cv2.imshow("Original Image", img)
            cv2.imshow("RGB Image", rgb)
            cv2.waitKey(0)
        elif index=="2":
            hsi = cv2.cvtColor(img, cv2.COLOR_RGB2HSV_FULL)
            cv2.imshow("Original Image", img)
            cv2.imshow("HSI Image", hsi)
            cv2.waitKey(0)
        else:
            console.print("Böyle bir ödev mevcut değil",style="error")
       
        
        
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")