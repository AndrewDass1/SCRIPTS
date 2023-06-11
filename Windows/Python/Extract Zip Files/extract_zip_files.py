#!/usr/bin/env python3

import os
import glob
from zipfile import ZipFile

path = os.getcwd()
files = glob.glob('*.zip')
index = 0

if path == r"":
	for i in range(0, len(files)):
		with ZipFile(files[index], mode='r') as zip:
			zip.extractall()
			print("Extraction completed! " + str(files[index]) + " has been extracted!")
		index += 1
else:
	print("Not the specified directory. Go to the specified directory and it must contain this Python Script to extract all zip files.")
