import argparse
import glob
import json
import os
import pprint
import re
import shutil

import yaml


def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# parser = argparse.ArgumentParser()
# parser.add_argument('dir', help='input dir')
# args = parser.parse_args()  


files = sorted(glob.glob("/home/digital/sgk/data/nuscene/sweeps/CAM_FRONT/*.jpg"), key=numericalSort)
f = open("video.txt", "w")    

for str_file in files:
    print(str_file)
    # filename = str_file.split('.')
    f.write("file '" + str_file + "'\n")
    f.write("duration 0.0833\n")
    
