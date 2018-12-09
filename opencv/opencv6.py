import cv2


#HUE = 0-180 , SETUARATION = 2-255 , VOLUME=0-255

img= cv2.imread("team1.png")

img_HSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv img", img_HSV)
cv2.imshow('hue chanel:', img_HSV[:,:,0])
cv2.imshow('saturationchanel:' ,img_HSV[:,:,1])
cv2.imshow(' volume chanel:',img_HSV[:,:,2])

cv2.waitKey(0)
cv2.destroyAllWindows()