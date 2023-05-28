#!/usr/bin/python3                                                                                                                                                                                                                                                        import subprocess                                                                                                                                                                                                                                                         subprocess.run("echo Hey")

import os
import glob
from zipfile import ZipFile

path = os.getcwd()
files = glob.glob('*.zip')
print(files[0])

if path == r"":
	for i in files:
		num_increment = 0
		with ZipFile(files[num_increment], mode='r') as zip:
			zip.extractall()
			print("Extraction completed!")
		num_increment += 1
else:
	print("Not directory")
