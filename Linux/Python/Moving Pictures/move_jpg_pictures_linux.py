#!/usr/bin/env python3

import os, glob, shutil

download_path = os.getcwd()

jpg_images = glob.glob("*.jpg")
picture_JPG_entry = 0

if download_path == r"insert_file_download_path":
    for i in jpg_images:
        current_image = jpg_images[picture_JPG_entry]
        str_current_image = str(current_image)

        original_path = str_download_path + "/" + str_current_image
        print(original_path)

        shutil.move( os.path.abspath(str_current_image), os.path.abspath(r"directory_path_where_pictures_will_be_moved_to") + "/" + str_current_image )

        picture_JPG_entry += 1

    print("Success. Images moved!")
else:
    print("Not in the same directory. No images moved.")
