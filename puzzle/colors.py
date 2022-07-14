from PIL import Image
import cv2, random, numpy as np
from piece import *

imgdir = "C:\\Users\\ek\\Desktop\\sdfghj\\puzzle\\testimgs"

ref = np.array(cv2.imread(f"{imgdir}\\turtle\\reference.jpg"))
sample = np.array(cv2.imread(f"{imgdir}\\turtle\\pc1cr.jpg"))

ref = cv2.GaussianBlur(ref, (5,5), 60)
sample = cv2.GaussianBlur(sample, (5,5), 60)

fref = ref[:,:,2]
fsample = sample[:,:,2]

#sampf = imutils.rotate(sampf, -1)
#fref = cv2.Sobel(fref, cv2.CV_16S, 1, 1, ksize=31)
#fsample = cv2.Sobel(fsample, cv2.CV_16S, 1, 1, ksize=31)
fref = cv2.Canny(image=fref, threshold1=50, threshold2=150)
fsample = cv2.Canny(image=fsample, threshold1=50, threshold2=150)

#bin = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)

cv2.imshow('reference', imscale(ref, .2))
cv2.imshow('filtered reference', imscale(fref , .2))
cv2.imshow('filtered sample', imscale(fsample, .2))
cv2.imshow('sample', imscale(sample, .2))
cv2.waitKey(0)