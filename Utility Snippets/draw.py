import cv2

frame=cv2.imread("00130.jpeg")

cv2.rectangle(frame, (601,431), (626,456), (255, 255, 00), 2)
cv2.imshow("frame",frame)
cv2.waitKey(0)
