import sys
import os
from PIL import Image

# Grab path of JPEG and new path for PNG
input_path = sys.argv[1]
output_path = sys.argv[2]
new_filetype = sys.argv[3]

# If new path doesn't exists, create directory
if not os.path.exists(output_path):
    os.makedirs(output_path)

# for each file in folder open, then remove extention and save as new filetype
for file in os.listdir(input_path):
   image = Image.open(f'{input_path}/{file}')
   file = os.path.splitext(file)[0]
   image.save(f"{output_path}/{file}.{new_filetype}",f'{new_filetype}')
