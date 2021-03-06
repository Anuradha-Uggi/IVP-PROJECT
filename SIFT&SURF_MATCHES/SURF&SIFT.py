# -*- coding: utf-8 -*-
"""SURF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17qfHoDyq6WL1DXDVOJ78-LNaKBBaGz-Q

**SIFT AND SURF CODES**
"""

! pip install opencv-contrib-python==3.4.2.17

from google.colab import files
files.upload()
files.upload()

"""**SURF CODE**"""

!pip install opencv-contrib-python-nonfree


import cv2
from pylab import *
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

def extract_surf_features(img):
    # sift_initialize = cv2.xfeatures2d.SIFT_create()
     surf = cv2.xfeatures2d.SURF_create()
     key_points, descriptors = surf.detectAndCompute(img, None)
     return key_points, descriptors

def showing_surf_features(img1, img2, key_points):
     return plt.imshow(cv2.drawKeypoints(img1, key_points, img2.copy()))

# # THE BELLOW CODE DOESN'T WORK IF THE IMAGES HAVE UNICODE CHARACTERES IN THEIR PATH
# # OpenCV does not accept it
# # So the files are directly inside the '../input' folder I don't know why:
img1 = cv2.imread('2011_001407.jpg')
img2 = cv2.imread('2010_004184.jpg')

# # converting to gray:
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# #Key points:
img1_key_points, img1_descriptors = extract_surf_features(img1_gray)
img2_key_points, img2_descriptors = extract_surf_features(img2_gray)

print('Displaying SURF features:')
showing_surf_features(img1_gray, img1, img1_key_points)
#showing_surf_features(img2_gray, img2, img2_key_points)

norm = cv2.NORM_L2
bruteForce = cv2.BFMatcher(norm)
matches = bruteForce.match(img1_descriptors, img2_descriptors)

matches = sorted(matches, key = lambda match:match.distance)
matched_img = cv2.drawMatches(
img1, img1_key_points,
img2, img2_key_points,
matches[:100], img2.copy())
plt.figure(figsize=(100,100))
plt.imshow(matched_img)

print('detected keypoints in img1:',len(img1_key_points))
print('detected descriptors in img1:',len(img1_descriptors))
print('detected keypoints in img2:',len(img2_key_points))
print('detected descriptors in img2:',len(img2_descriptors))

"""**SIFT CODE**"""

!pip install opencv-contrib-python-nonfree


import cv2
from pylab import *
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

def extract_sift_features(img):
     sift_initialize = cv2.xfeatures2d.SIFT_create()
     key_points, descriptors = sift_initialize.detectAndCompute(img, None)
     return key_points, descriptors

def showing_sift_features(img1, img2, key_points):
     return plt.imshow(cv2.drawKeypoints(img1, key_points, img2.copy()))

# # THE BELLOW CODE DOESN'T WORK IF THE IMAGES HAVE UNICODE CHARACTERES IN THEIR PATH
# # OpenCV does not accept it
# # So the files are directly inside the '../input' folder I don't know why:
img1 = cv2.imread('2010_004184.jpg')
img2 = cv2.imread('2011_001407.jpg')

# # converting to gray:
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# #Key points:
img1_key_points2, img1_descriptors2 = extract_sift_features(img1_gray)
img2_key_points2, img2_descriptors2 = extract_sift_features(img2_gray)

print('Displaying SIFT features:')
showing_sift_features(img1_gray, img1, img1_key_points2)

norm = cv2.NORM_L2
bruteForce = cv2.BFMatcher(norm)
matches = bruteForce.match(img1_descriptors2, img2_descriptors2)

matches = sorted(matches, key = lambda match:match.distance)
matched_img = cv2.drawMatches(
img1, img1_key_points,
img2, img2_key_points,
matches[:100], img2.copy())
plt.figure(figsize=(100,300))
plt.imshow(matched_img)

print('detected keypoints in img1:',len(img1_key_points2))
print('detected descriptors in img1:',len(img1_descriptors2))
print('detected keypoints in img2:',len(img2_key_points2))
print('detected descriptors in img2:',len(img2_descriptors2))

