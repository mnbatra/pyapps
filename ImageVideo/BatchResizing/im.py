import cv2

img=cv2.imread("galaxy.jpg",0)

print(img)
print(img.shape)
print(img.ndim)
l=int(img.shape[1]*0.5)
b=int(img.shape[0]*0.5)

resized=cv2.resize(img,(l,b))
cv2.imwrite("SmallGalaxy.jpg",resized)
cv2.imshow("Galaxy",resized)    
cv2.waitKey(0)
cv2.destroyAllWindows()
