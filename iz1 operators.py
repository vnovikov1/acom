import cv2
import numpy as np
import matplotlib.pyplot as plt

 
def roberts_operator(grayImage):
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)
    x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
    y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    
    return Roberts

def prewitt_operator(grayImage):
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
    x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
    y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    Prewitt = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    return Prewitt

def sobel_operator(grayImage):
    x = cv2.Sobel (grayImage, cv2.CV_16S, 1, 0) 
    y = cv2.Sobel (grayImage, cv2.CV_16S, 0, 1) 

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)

    Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    return Sobel


def main():
    img = cv2.imread('images\images.jpg')
    img = cv2.resize(img, (900,800))

    img_RGB = cv2.cvtColor (img, cv2.COLOR_BGR2RGB) 
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    plt.subplot (221), plt.imshow (img_RGB), plt.title ('Source image'), plt.axis ('off') 
    plt.subplot (222), plt.imshow (roberts_operator(grayImage), cmap = plt.cm.gray), plt.title ('Roberts'), plt.axis ('off')
    plt.subplot (223), plt.imshow (prewitt_operator(grayImage), cmap = plt.cm.gray), plt.title ('Prewitt'), plt.axis ('off')
    plt.subplot (224), plt.imshow (sobel_operator(grayImage), cmap = plt.cm.gray), plt.title ('Sobel'), plt.axis ('off')
    plt.show()


main()