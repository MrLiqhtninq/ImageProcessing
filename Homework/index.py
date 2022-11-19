import random
import os
import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image
from rich.console import Console
from rich.theme import Theme 
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)
imgPath = '/Users/mrliqhtninq/Desktop/ImageProcessing/images/lake.jpeg'
bookPath = '/Users/mrliqhtninq/Desktop/ImageProcessing/images/book.jpg'

def BitChange(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    image.show(title=str(pixel_size)+"Bit Image")
    
    
def GrayScaleToBit():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        bits = [8,16,24]
        
        saveImgPath = '/Users/mrliqhtninq/Desktop/ImageProcessing/images/graylake.jpeg'
        
        Image.open(imgPath).convert('RGB').convert('L').save(saveImgPath)
        
        for index in range(3):
            BitChange(saveImgPath,bits[index])
        image = Image.open(saveImgPath)
        image.show()
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")
        
        
def Gama():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        img = cv2.imread(imgPath)
        gama3 = np.array(255*(img / 255) ** 3.0, dtype = 'uint8')
        gama4 = np.array(255*(img / 255) ** 4.0, dtype = 'uint8')
        gama5 = np.array(255*(img / 255) ** 5.0, dtype = 'uint8')
        Concated = np.concatenate((img, gama3, gama4, gama5), axis=1)
        cv2.imshow('Gama', Concated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")
        
def LogTransformation():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        image = cv2.imread(imgPath)
        c= 255/np.log(1+np.max(image))
        log_image = c * (np.log(image+1))
        log_image = np.array(log_image, dtype = np.uint8)
        
        Concated = np.concatenate((image, log_image), axis=1)
        cv2.imshow('Log Transformation', Concated)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")

def toNegative(photo):
    L=np.max(photo)
    negative=L-photo
    return negative

def ImageToNegative():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        img = cv2.imread(imgPath)
        negative= toNegative(img)

        plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.imshow(negative,cmap = 'gray')
        plt.title('Negative'), plt.xticks([]), plt.yticks([])
        
        plt.show()
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")
        
def TextFixer():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        image = cv2.imread(bookPath)
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 35)


        Concated = np.concatenate((image, adaptive), axis=1)
        cv2.imshow('Text Fixer', Concated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")
        
def Filter():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Gaussian
        gauss = cv2.GaussianBlur(gray,(3,3),0)
        #Laplacian
        laplacian = cv2.Laplacian(gauss,cv2.CV_64F)
        #Sobel
        sobelx = cv2.Sobel(gauss,cv2.CV_64F,1,0,ksize=5)  # x
        sobely = cv2.Sobel(gauss,cv2.CV_64F,0,1,ksize=5)  # y

        #Prewitt
        kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        prewittx = cv2.filter2D(gauss, -1, kernelx)
        prewitty = cv2.filter2D(gauss, -1, kernely)
        
        #Robert Cross
        roberts_cross_v = np.array( [[ 1, 0 ], [ 0, -1 ]] )
        roberts_cross_h = np.array( [[ 0, 1 ], [ -1, 0 ]] )
        imgRobert = cv2.imread(imgPath,0).astype('float64')
        imgRobert/=255.0
        vertical = ndimage.convolve( imgRobert, roberts_cross_v )
        horizontal = ndimage.convolve( imgRobert, roberts_cross_h )
        edgedRobert = np.sqrt( np.square(horizontal) + np.square(vertical))
        edgedRobert*=255
        
        # total_rows, total_columns, subplot_index(1st, 2nd, etc..)
        plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,2),plt.imshow(gray,cmap = 'gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,3),plt.imshow(laplacian,cmap = 'gray')
        plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,4),plt.imshow(gauss,cmap = 'gray')
        plt.title('Gaussian'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,5),plt.imshow(prewittx,cmap = 'gray')
        plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,6),plt.imshow(prewitty,cmap = 'gray')
        plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,7),plt.imshow(sobelx,cmap = 'gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,8),plt.imshow(sobely,cmap = 'gray')
        plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,9),plt.imshow(edgedRobert,cmap = 'gray')
        plt.title('Robert Cross'), plt.xticks([]), plt.yticks([])

        plt.show()
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")


def addNoise(image):
    row , col = image.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        image[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        image[y_coord][x_coord] = 0
    return image

def SaltAndPepper():
    console.print("Çıkmak için CTRL+C",style="error")
    try:
        saveImgPath = '/Users/mrliqhtninq/Desktop/ImageProcessing/images/saltandpepper.jpg'
        image = cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(saveImgPath, addNoise(image))

        print(image)
        print(image.ravel())
        plt.hist(image.ravel(),256,[0,256])
        plt.title('Histogram')
        cv2.imshow('Noise Image', image)
        plt.show()
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        console.print("Script Sonlandırıldı!",style="success")
