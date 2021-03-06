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
        else:
            os.rename(LOAD_DIR + file, FAILED_DIR + file)  # If it's not an image, it fails


def get_custom_name():
    y_or_n = ['y', 'n']
    change = ''
    while change not in y_or_n:
        change = input('Would you like to rename all images to have the same name? [y|n]: ').lower()

    if change == 'y':
        confirm = 'n'
        while confirm != 'y':
            name_input = input('What would you like to name the images? ')
            print(f'You entered \"{name_input}\". The images will be named like this: \"2022-07-13_{name_input}.\"')
            confirm = input('Is this correct? [y|n]: ').lower()
        return name_input
    else:
        return 'no'


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

# see if the user wants to use a new name
custom_name = get_custom_name()

# dictionary to hold the dates to make sure the same name doesnt get made twice
date_dict = {}

# loop through the images and convert the names
for original_file_name in image_files:
    try:
        image = Image.open(LOAD_DIR + original_file_name)  # get the image object from the file
    except:
        print(f'{original_file_name} is not a jpg. Moved to failed folder.')
        os.rename(LOAD_DIR + original_file_name, FAILED_DIR + original_file_name)  # move the file to the failed dir
        continue
    try:
        date = get_formatted_date_string_from_image(image)
    except:
        print(f'Date not found for this image: {original_file_name}.')
        date = 'earlier'

    if custom_name == 'no':
        new_name = drop_default_date_if_found(original_file_name)
    else:
        new_name = custom_name

    if date not in date_dict:
        date_dict[date] = [1]
        final_name = f'{date}_{new_name}.jpg'
        os.rename(LOAD_DIR + original_file_name, MODIFIED_DIR + final_name)  # move the file to the modified directory
    else:
        count = len(date_dict[date]) + 1
        final_name = f'{date}_{new_name}({count}).jpg'
        date_dict[date].append(count)
        os.rename(LOAD_DIR + original_file_name, MODIFIED_DIR + final_name)  # move the file to the modified directory

