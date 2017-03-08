import numpy as np
import os
from scipy.misc import *
import cv2

directory='/home/mpcr/Documents/MT/Heat_maps/Gaze'
os.chdir(directory)
out=sum([len(files) for r, d, files in os.walk(os.getcwd())])
out=np.zeros([out, 1280, 1024])

im_num=0

for folder in os.listdir(os.getcwd()):
  os.chdir(folder)
  for f in os.listdir(os.getcwd()):
    print(f)
    with open(f) as g:
      gazedata = np.genfromtxt(f, dtype=np.int32, delimiter='\t', skip_header=0, usecols=(2))
      xgazedata = np.genfromtxt(f, dtype=np.int32, delimiter='\t', skip_header=0, usecols=(0))
      ygazedata = np.genfromtxt(f, dtype=np.int32, delimiter='\t', skip_header=0, usecols=(1))
      r=np.asarray(np.where(xgazedata!=-2147483648))
      xgazedata=xgazedata[r[0, :]]
      ygazedata=ygazedata[r[0, :]]

    for i in range(len(ygazedata)):
      out[im_num, xgazedata[i], ygazedata[i]]+=255

    out[im_num, :, :]=cv2.blur(out[im_num, :, :],(5,5))
    im_num+=1
  os.chdir(directory)

