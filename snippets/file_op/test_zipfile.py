import os
# from zipfile import ZipFile
import shutil


dir_name = "test_zip"

if os.path.isdir(dir_name):
    shutil.rmtree(dir_name)

os.mkdir(dir_name)

if os.path.isfile('{}.zip'.format(dir_name)):
    os.remove('{}.zip'.format(dir_name))

shutil.make_archive(dir_name, 'zip', dir_name)
