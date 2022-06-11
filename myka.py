import cv2
filepath ="kobe.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("My Favorite number <3",image)
cv2.waitKey(0)
cv2.destroyAllWindows()