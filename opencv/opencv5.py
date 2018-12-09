import cv2
img=cv2.imread("team1.png",0)
cv2.imshow("yy",img)
cv2.waitKey(0)
ret, bw = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
cv2.imshow("binary",bw)
print(img.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()