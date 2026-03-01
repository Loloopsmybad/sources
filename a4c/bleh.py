import cv2
import numpy as np
import matplotlib as plt

a = cv2.VideoCapture(1)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('capture.avi',fourcc,20.0,(640, 480))

while True:
    ret, b= a.read()
    cv2.imshow('blahhhh',b)
    #out.write(b)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
#a.release()
out.release()
cv2.destroyAllWindows()

