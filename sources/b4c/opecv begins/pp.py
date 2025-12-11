'''

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile
from urllib.request import urlretrieve
import cv2



cam=cv2.VideoCapture(0)

width=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret,f= cam.read()

    cv2.imshow('camera',f)

    if cv2.waitKey(1)==ord('q'):
            break
cam.release()
cv2.destroyAllWindows()
    
'''



def lmao(num):
    for i in range(len(num)):
        if num[i] % 2 == 0 :
            num[i]= num[i]+1

num=[1,2,3,4,5,6,7]
x= 3
for i in range(x):
    lmao(num)
    num.append(num[i]*2)
    x = len(num)

print(num)