import sys
import os
from PIL import Image

# grab first and second argument
try:
	source_folder = sys.argv[1]
	result_folder = sys.argv[2]
	if '/' not in source_folder:
		source_folder = source_folder+'/'
	if '/' not in result_folder:
		result_folder = result_folder+'/'
except IndexError as err:
	print('Please enter the source folder name and result folder name.')
	raise err

# check if result folder exists, if not create one
if os.path.isdir(result_folder):
	print(f'The images are going to be converted into PNG in {result_folder}, please wait.')
else:
	os.mkdir(result_folder)
	print(f'A New folder {result_folder} has been created to save the converted images, please wait.')

# loop through pokedex, convert images into png, save to the new folder
for file in os.listdir(source_folder):
	if file.endswith(".jpg"):
		img = Image.open(f'{source_folder}{file}')
		clean_name = os.path.splitext(file)[0]
		img.save(f'{result_folder}{clean_name}.png','png')

print('All of the JPG images have been converted!')

