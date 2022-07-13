import os
from os import listdir
from PIL import Image

# Directory paths
FAILED_DIR = 'failed/'
LOAD_DIR = 'load/'
MODIFIED_DIR = 'modified/'

# an array to hold all the images from the load directory
image_files = []


# --------------------- DEFINE FUNCTIONS
def get_images():
    all_files_in_load = [file for file in listdir(LOAD_DIR)]  # grab all the files in the load directory
    for file in all_files_in_load:  # loop through the files
        if file[-3:] == 'jpg':  # if it's an image, add it to the image_files array
            image_files.append(file)


def get_formatted_date_string_from_image(jpg):
    raw_date = jpg._getexif()[36867]  # this is the reference for the created date in the image metadata
    year = raw_date[:4]  # the first four characters are the year value
    month = raw_date[5:7]  # the fifth and six characters are the month value
    day = raw_date[8:10]  # the eighth and ninth characters are the day value
    return f'{year}-{month}-{day}'  # format and return the date


def drop_default_date_if_found(name):
    if name[:8].isnumeric():  # if the first 8 characters are numeric, it's the un-formatted date
        name = name[8:]  # drop the original date
        if name[0] == "_":
            name = name[1:]  # drop the underscore
    return name


# --------------------- SCRIPT FLOW BEGINS

# get all images from the load folder
get_images()

# loop through the images and convert the names
for file in image_files:
    try:
        image = Image.open(LOAD_DIR + file)  # get the image object from the file
    except:
        print(f'{file} is not a jpeg. Moved to failed folder.')
        os.rename(LOAD_DIR + file, FAILED_DIR + file)  # move the file to the failed directory
        continue
    try:
        date = get_formatted_date_string_from_image(image)
    except:
        print(f'Date not found for this image: {file}.')
        os.rename(LOAD_DIR + file, FAILED_DIR + file)  # move the file to the failed directory
        continue

    filtered_name = drop_default_date_if_found(file)
    new_name = f'{date}_{filtered_name}'
    os.rename(LOAD_DIR + file, MODIFIED_DIR + new_name)  # move the file to the modified directory
