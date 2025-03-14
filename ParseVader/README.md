# ParseVader <'_'>
# - An Image Organizer by Date

This Python project organizes and filters images based on their modification timestamps, using OpenCV and the os module.

## Features

Recursively scans a main directory containing image subdirectories

Filters images by file extension (.png, .jpg, .jpeg)

Extracts and formats modification timestamps

Selects images modified today

Sorts images by most recent modification time

## Requirements

Ensure you have the following installed:

- Python 3.x

- OpenCV (cv2)

### Install dependencies using:

'''python
 pip install opencv-python

## Setup

- Update img_main_dir with the absolute path of your image directory.
- **If you want all images, not just those modified today, comment out the *today =* line and the subsequent conditional.**

Run the script:

'''python
 python dir_parser.py

### Output

A dictionary of images modified today, sorted by latest modification time, will be printed to the console.

## Future Improvements

- Optimize resource usage by reducing nested loop complexity

- Implement parallel processing for better performance

## License

This project is open-source and available under the **MIT License**.

