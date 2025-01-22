import cv2
img = cv2.imread("20250101_141751.JPG")
reimg = cv2.resize(img, dsize=None, fx=0.2, fy=0.2)
crimg = cv2.cvtColor(reimg, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", crimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#if img is None: 
#    print('Failed to load image')