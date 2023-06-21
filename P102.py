import os
import shutil

source='C:/Users/abdbe/Desktop/C102folderA/source'

dest='C:/Users/abdbe/Desktop/C102folderA/dest'

list_of_files = os.listdir(source)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = source + '/' + file_name
        path2 = dest + '/' + "Document_Files"
        path3 = dest + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + "......")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + "......")
            shutil.move(path1,path3)