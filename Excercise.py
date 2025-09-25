
#Imports the os module so you can interact with the file system
#list directories, join paths, check if something is a directory, etc.

import os

def list_dir(s): # define function that takes a path 's'

    def dir_list(d):            #define inner function to list directories inside path 'd'
        nonlocal tap_stop       #use tap_stop variable from outer function
        files = os.listdir(d)   #gets a list of names (files and subdirectories) inside directory

        # loop through each file/folder in current directory
        for f in files:
            current_dir = os.path.join(d, f) #make full path for file/folder

            if os.path.isdir(current_dir): #checks if the current path is a directory.
                print('\t'*tap_stop + 'directory' + f)
                tap_stop += 1
                dir_list(current_dir)
                tap_stop -= 1
            else:
                print(f)
    tap_stop = 0
    # in this S is argument to check if the path is correct
    if os.path.exists(s):
        #search all the files
        print('Directory Listing of' + s)
        dir_list(s)
    else:
        print(s+'Directory does not exist')

# call function with given path

list_dir('C:\\Users\\Arena Multimedia\\PyCharmMiscProject')
