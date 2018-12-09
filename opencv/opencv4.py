import cv2
img= cv2.imread('f.jpg',0)




cv2.imshow('new color',img)
print(img.shape)



cv2.waitKey(0)

cv2.destroyAllWindows()