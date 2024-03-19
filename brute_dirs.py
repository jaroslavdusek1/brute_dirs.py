#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:
    A Python script designed to inspect and display the structure of directories and files
    starting from a user-specified root directory. It provides a hierarchical view of folders
    and files, allowing users to understand the organization of directories and their contents.

Maintainer:
            ::::  ::::::::::::  
            :+:     :+:    :+: 
            +:+     +:+    +:+ 
            +#+     +#+    +:+ 
            +#+     +#+    +#+ 
        #+# #+#     #+#    #+# 
         #####    ############     

Date:
    Mar 01, 2024

Usage:
    python3 brute_dirs.py

Dependencies:
    - os library for interacting with the operating system's directory structure.

Notes:
    The script traverses the directory tree starting from the specified root directory and
    displays all subdirectories and files, reflecting their hierarchical structure. It aims
    to provide a clear and concise representation of the directory contents.
"""

# ascii art welcome
print("""                                                   
8                     o                   8  o                               
8                     8                   8                                  
8oPYo. oPYo. o    o  o8P .oPYo.      .oPYo8 o8 oPYo. .oPYo.    .oPYo. o    o 
8    8 8  `' 8    8   8  8oooo8      8    8  8 8  `' Yb..      8    8 8    8 
8    8 8     8    8   8  8.          8    8  8 8       'Yb.    8    8 8    8 
`YooP' 8     `YooP'   8  `Yooo'      `YooP'  8 8     `YooP' 88 8YooP' `YooP8 
:.....:..:::::.....:::..::.....:oooo :.....::....:::::.....:..:8 ....::....8 
::::::::::::::::::::::::::::::::.....::::::::::::::::::::::::::8 :::::::ooP'.
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::::...::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")

import os

import os

class DirectoryLister:
    def __init__(self, start_path):
        self.start_path = start_path

    def list_files_and_directories(self):
        """Walk through the directory tree and print out each directory and file."""
        for root, dirs, files in os.walk(self.start_path):
            level = root.replace(self.start_path, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f'{indent}{os.path.basename(root)}/')
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f'{subindent}{f}')

# Prompt the user for the starting directory
start_path = input("Set a start path: ")
directory_lister = DirectoryLister(start_path)

# Call the method to list directories and files
directory_lister.list_files_and_directories()
