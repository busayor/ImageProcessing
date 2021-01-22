import sys
import os
from PIL import Image

# we want to run python3 JPGtoPNGConverter.py Pokedex/new/
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

# grab first and second argument
# use path,exists to search if the folder exists
if not os.path.exists(output_folder):
	# use makedirs to create a new folder
	os.makedirs(output_folder)

ext=['.jpg','.png','.gif']
for filename in os.listdir(image_folder):
	img_ext = os.path.splitext(filename)[1]
	clean_name = os.path.splitext(filename)[0]
	# print(clean_name)
	if img_ext in ext:
		img = Image.open(f'{image_folder}{filename}')
		img.save(f'{output_folder}{clean_name}.png', 'png')
		print('all done!!')

# check if new/ exists, else create it

# loop through Pokedex

# convert images from jpg to png

#  save them to the new folder