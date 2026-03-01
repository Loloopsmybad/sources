'''import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(0):
        
        break
#Release everything if job is finished
cap.release()
cv2.destroyAllWindows ()
'''
import cv2
import numpy as np
import matplotlib as plt

a = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('capture.avi',fourcc,20.0,(640, 480))

while True:
    ret, b= a.read()
    print(b.shape[1])
    cv2.imshow('blahhhh',b)
    
    #out.write(b)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
a.release()
#out.release()
cv2.destroyAllWindows()

