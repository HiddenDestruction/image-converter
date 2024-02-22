
import os
import glob

# Specify the directory you want to start from
rootDir = os.getcwd()

# Find all .jpeg files in the directory
for filename in glob.iglob(rootDir + '**/*.jpeg', recursive=True):
    # Construct new filename by replacing .jpeg with .jpg
    new_filename = filename.rsplit(".", 1)[0] + ".jpg"
    
    # Rename the file
    os.rename(filename, new_filename)