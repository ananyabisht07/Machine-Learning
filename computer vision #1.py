import cv2

#reading the images
img1=cv2.imread('1.jpeg',1)
img2=cv2.imread('2.jpeg',1)

#cropping the same size of both of the images
crop1=img1[200:400,200:300]
crop2=img2[200:400,200:300]

#pasting the cropped parts of the images to another image
img2[:crop1.shape[0],:crop1.shape[1]]=crop1
img1[:crop2.shape[0],:crop2.shape[1]]=crop2

#displaying the final images
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey(0)