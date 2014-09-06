"""
Crawling all the pictures  in the file system
and move them to mentioned folder in year wise fasion.
"""
import exifread
from os.path import walk
from os import path
import os 
import shutil
from glob import glob

file_list = {}
dest =  'D:\Pictures\Others'
def process_pics(args, dir, fnames):
	"""
	copies Files in the desired folders
	"""
	for file in fnames:
		if file.endswith('.jpg'):
			file = path.join(dir, file)
			f = open (file, 'rb')
			exif = exifread.process_file(f)
			f.close()
			if 'Image DateTime' in exif:
				dirname =  str(exif['Image DateTime'])[:4]
				destination  = os.path.join(dest, dirname)
				if not path.exists(destination):
					os.makedirs(destination)
				shutil.copy2(file, destination)
			
dirs = ['C:/','D:/','E:/']
for dir in dirs:
	walk(dir, process_pics, None)
print 'Done'