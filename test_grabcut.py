import cv2
import numpy as np
import sys
import os

img = cv2.imread('/home/symao/Pictures/3773.png')
mask = np.ones(img.shape[:2],np.uint8)*3
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
mask[:3,:] = cv2.GC_PR_BGD
cv2.grabCut(img,mask,None,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_MASK)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imshow('img',img)
cv2.imshow('m',mask2*128)
cv2.waitKey()