#!/usr/bin/env python3

import os
import glob
import shutil

download_path = os.getcwd()
str_download_path = str(download_path)

jpg_images = glob.glob("*.JPG")
picture_JPG_entry = 0

if download_path == r"":
    for i in jpg_images:
        current_image = jpg_images[picture_JPG_entry]
        str_current_image = str(current_image)

        original_path = str_download_path + "\\" + str_current_image
        print(original_path)

        shutil.move( os.path.abspath(str_current_image), os.path.abspath(r"") + "\\" + str_current_image )

        picture_JPG_entry += 1

    print("Success. Images moved!")
else:
    print("Not in the same directory. No images moved.")
