import cv2
import numpy as np
img2=cv2.imread('1.jpeg')
img1 = cv2.imread('2.jpeg')
merge = np.concatenate((img1, img2), axis=1)
print(img1.shape)
print(img2.shape)
#cv2.imshow('merged',merge)
cv2.imwrite('out.jpeg', merge)

diff = cv2.absdiff(img1, img2)
cv2.imwrite('dif.jpeg', diff)

cv2.imshow('merged',merge)
cv2.imshow('diff',diff)
cv2.waitKey(0)