#!/usr/bin/env python

import os
import numpy as np
import cv2
from PIL import Image
import torch
#import pdb

def main():
	s = os.getcwd() + '/1.bmp'
	#pdb.set_trace()
	img = cv2.imread(s)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img = img.astype(np.uint8)
	new_img = np.zeros((576, 576, 3)).astype(np.uint8)
	new_img[38:-38, 1:-1, :] = img
	#img = np.moveaxis(img, -1, 0)
	print(img.shape)
	print(new_img.shape)
	print(torch.from_numpy(np.moveaxis(new_img, -1, 0)).float().shape)
	test = Image.fromarray(new_img, 'RGB')
	test.save('testimg.bmp')

main()