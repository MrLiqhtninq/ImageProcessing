import os
import time
import cv2 
import pafy
import numpy as np
from rich.console import Console
from rich.theme import Theme 
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)

def Week5():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
       #Smoothing 
        img = cv2.imread('/Users/mrliqhtninq/Desktop/ImageProcessing/images/lake.jpeg')
        averaging =  cv2.blur(img,(5, 5))
        gaussian = cv2.GaussianBlur(img,(5, 5), 0)
        bilateral = cv2.bilateralFilter(img, 5, 75, 75)
        median = cv2.medianBlur(bilateral, 5)
        cv2.imshow("Original Photo", img)
        cv2.imshow("Averaging", averaging)
        cv2.imshow("Gaussian Photo", gaussian)
        cv2.imshow("Median Photo", median)
        cv2.imshow("Bilateral Photo", bilateral)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")