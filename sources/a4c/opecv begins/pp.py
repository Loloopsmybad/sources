import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile
from urllib.request import urlretrieve
import cv2




cb_img = cv2.imread("logo.png",0)

plt.imshow(cb_img, cmap="gray")


plt.imshow(cb_img)