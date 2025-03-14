import os
import cv2
from datetime import datetime
from datetime import date

img_main_dir = r"C:\Users\New\Path_to_master_folder"#Absolute path to the main directory containing a collection of images

images_dict = {} #Created an empty dictionary to store my images

for subdirectory in os.listdir(img_main_dir):#loop over all subdirectories in the main directory
    sub_dir_path = os.path.join(img_main_dir, subdirectory)
    for filename in os.listdir(sub_dir_path):#Looping through the subdirectory
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):#Filtering images by their extensions
            img_path = os.path.join(sub_dir_path, filename) #Merging the subdirectory path and the filename to create an absolute path to each individual image
            img = cv2.imread(img_path)#use cv2 to read the image
            if img is not None:
                timestamp = os.stat(img_path)
                image_time = timestamp.st_mtime #extract the datestamp property from image statistics.
                datetime_r = datetime.fromtimestamp(image_time).strftime('%Y-%m-%d %H:%M:%S')
                today = datetime_r.startswith(date.today().strftime('%Y-%m-%d %H:%M:%S')) #only chooses the images modified at current date.
                if today is True:
                    images_dict[filename] = (img_path, datetime_r)
                # Now we append all these images into our dictionary.

sorted_images = dict(sorted(images_dict.items(),key=lambda item :item[1][1], reverse = True)) # Sort the images by latest first.
print(sorted_images)

#Still a bit much resource intensive - with all the complexities from the nested loops. Will work on that soon. Expect an update.