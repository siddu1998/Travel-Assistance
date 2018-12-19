import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('00377.jpeg',0)
equ = cv2.equalizeHist(img)
cv2.imwrite('res.jpeg',equ)