import cv2
import numpy as np
import matplotlib as plt

a =cv2.imread('logo.png')

cv2.line(a,(0,150),(150,200),(255,0,0),3)
point=np.array([[0,255],[200,400],[300,500]],np.int32)
cv2.polylines(a , [point] ,True,(255,200,255),99)

cv2.imshow('nigger',a)
cv2.waitKey(0)
cv2.destroyAllWindows()

