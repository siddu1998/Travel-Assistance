import cv2
img = cv2.imread('00001.jpeg')
height, width, channels = img.shape 
print(width,height)