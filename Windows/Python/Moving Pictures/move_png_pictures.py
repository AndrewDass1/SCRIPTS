#!/usr/bin/env python3

import os
import glob
import shutil

download_path = os.getcwd()

png_images = glob.glob("*.png")
picture_png_entry = 0

if download_path == r"insert_file_download_path":
	for i in png_images:
		current_image = png_images[picture_png_entry]
		str_current_image = str(current_image)

		original_path = download_path + "\\" + str_current_image		
		print(original_path)

		shutil.move( os.path.abspath(str_current_image), os.path.abspath(r"directory_path_where_pictures_will_be_moved_to") + "\\" + str_current_image )

		picture_png_entry += 1

	print("Success. Images moved!")
else:
	print("Not in the same directory. No images moved.")
