#coding:utf-8

import zipfile
from zipfile import PyZipFile
from zipfile import ZipFile

print(zipfile.is_zipfile("ZIP.zip"))

"""zipfile.ZipFile("ZIP.zip" , mode = 'r' , compression=ZIP_STORED , allowZip64=True , compresslevel=None)
with ZipFile('ZIP.zip', 'w') as myzip:
	myzip.write('eggs.txt')
	ZipFile.close("ZIP.zip")

"""

with ZipFile('ZIP.zip', 'w') as myzip1:
	myzip1.write('texte.txt')

with ZipFile('ZIP.zip') as myzip:
	with myzip.open('texte.txt') as myfile:
		print(myfile.read())




ZipFile.close('ZIP.zip')