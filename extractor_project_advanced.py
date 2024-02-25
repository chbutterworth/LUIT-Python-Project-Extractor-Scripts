#!/usr/bin/env python3

import os

def extractor():
    
    file_info = []

    for dirpath, dirnames, filenames in os.walk(the_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_size = os.path.getsize(file_path)
            file_info.append({"name": file, "size": file_size})

    print("------------------------------------")
    print(*file_info, sep="\n")
    print("------------------------------------")

print("Enter pathway for script to scan.")
the_path = input()

if os.path.exists(the_path) == False:
    the_path = os.getcwd()
    print("---invalid path provided---")
    print("---defaulting to current working directory---")
    confirm = input("proceed y/n?  ")
    if confirm == "n":
        print()
        print("---ending script---")
        print()
        quit()
    elif confirm != "y":
        print("Derp")
        print()
        print("---ending script---")
        quit()
    else:
        print("---proceeding---")
        print()
        extractor()
else:
    print("---valid path entered---")
    print("---proceeding---")
    print()
    extractor()