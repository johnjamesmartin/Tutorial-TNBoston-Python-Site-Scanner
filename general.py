# Imports:

import os


# Did we create folder? If not, create it:

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Write file:

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()