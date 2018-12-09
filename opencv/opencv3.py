import cv2
img=cv2.imread('f.jpg')
cv2.imshow("output",img)
print(img.shape)
print('height pixel value:',img.shape[2])


cv2.waitKey(0)

cv2.destroyAllWindows()