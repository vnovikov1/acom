import cv2
import math
import numpy as np


def gray1():
    gray = cv2.imread(r'C:\multi\images\colors.png', cv2.IMREAD_GRAYSCALE)
    gray = cv2.resize(gray, (600,500))
    new_gray = gray.copy

    N = 5
    M = 5
    A = [[0]*N for i in range(M)]

    sigma = 1
    pi = 3.14
    e = 2.71
    a = 2
    b = 2
    for i in range(N):
        for j in range(M):
            A[i][j] = (1/(2*pi*sigma**2))*e**(-((i-a)**2+(j-b)**2)/(2*sigma**2))

    print(A)
    sum = 0
    k = 0
    for i in range(N):
        for j in range(M):
            sum += A[i][j]

    print(sum)
    new_sum = 0
    for i in range(N):
        for j in range(M):
            A[i][j] = A[i][j] / sum
            new_sum += A[i][j]

    print(new_sum)
    
    

def gauss_():
    img1 = cv2.imread(r'C:\multi\images\colors.png', cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (600,600))
    img2 = img1.copy

    # cv2.imshow('Source gray', img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    N = 5
    M = 5
    A = [[0]*N for i in range(M)]

    a = M // 2 
    b = N // 2
    sigma = 1
   

    for i in range(N):
        for j in range(M):
            A[i][j] = (1/(2*math.pi*sigma**2))*np.exp(-((i - a)**2 + (j - b)**2)/(2*sigma**2))


    print(A)

    sum = 0
    k = 0

    for i in range(N):
        for i in range(M):
            sum =+ A[i][j]
            k += 1

    print('my sum - ' + str(sum))
    print(k)





def cv_gauss():
    img = cv2.imread(r'C:\multi\images\colors.png', cv2.IMREAD_COLOR)
    img_ = cv2.GaussianBlur(img, ksize=(15, 15), sigmaX=0, sigmaY=0)

    img = cv2.resize(img, (600,600))
    img_ = cv2.resize(img_, (600,600))

    cv2.imshow('Source image', img)
    cv2.imshow('Blur image',img_)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

gauss_()
# cv_gauss()