# Prepend Date On Picture Names
### Purpose
The purpose of this application is to take any image, and 
add a formatted date string to the beginning of the name.
### Example Input/Output
- "20190213_123918.jpg" -----> "2019-02-13_123918.jpg"
- "Old-Castle-In-England.jpg" -----> "2016-10-11_Old-Castle-In-England.jpg"
### Description
- Extract the date that the picture was taken, then add 
it to the beginning of the image name so that images 
will have a nicely formatted date to show when the 
photo was taken.
- If the photo name already begins with a date, but the 
date is in "yyyymmdd" format, the original date will be 
dropped in favor of the date in "yyyy-mm-dd" format
### Instructions for Use
1. Any photo who's name you want changed should be loaded 
into the "load" folder
2. Run the script
3. Remove your photos with the changed names from "modified"
folder
4. If any photos were unsuccessful, they will be in 
the "failed" folder
### New Functionality
1. Ask the user if they would like to name all the files
the same.
2. If they answer yes, prompt the user for the new name
- **This will allow the user to put all the images of 
one person in the load folder, then name them the same name.
For instance: "2022_07-13_James"**