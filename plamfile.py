import cv2
image = cv2.imread("palm.jpg")
cv2.imshow("plam",image)
cv2.waitkey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGRGRAY)
edges = cv2.Canny(gray,40,55,apertureSize = 3)
cv2.imshow("edges in plam",edges)
cv2.waitkey(0)
edges = cv2.bitwise_not(edges)