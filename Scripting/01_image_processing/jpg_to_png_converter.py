# python jpg_to_png_converter.py Pokedex/ new/ (on windows \)
'''
First arg is the folder contains jpeg files
Second arg is the name of the folder will be created.
'''

import sys
import os
from PIL import Image

# grap first and second argument
images_folder = sys.argv[1]
output_folder = sys.argv[2]

print(images_folder, output_folder)

# check if folder exists, if not, create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# converts images to png
# save to the folder.
for filename in os.listdir(images_folder):
    img = Image.open(f'{images_folder}{filename}')
    #clean the jpg from the name
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{filename}.png', 'png')
    print('all done !')
