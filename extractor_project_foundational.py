#!/usr/bin/env python3

import os

working_path = os.getcwd()

the_path = os.scandir(working_path)

file_info = []

for entry in the_path:
    file_path = entry.path
    file_name = entry.name
    file_size = entry.stat().st_size

    if entry.is_file() == True:
        file_info.append({'type': 'f', 'path': file_path, 'name': file_name, 'size': file_size})
    elif entry.is_dir() == True:
        file_info.append({'type': 'd', 'path': file_path, 'name': file_name, 'size': file_size})

print(*file_info, sep="\n")