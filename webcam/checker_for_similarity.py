#!/usr/bin/python

import sys
import subprocess
import json
import os
import glob


def curl(img1, img2):
    run = subprocess.check_output("bash ../shell_scripts/my_curl_script.sh " \
                                +img1+' ' \
                                +img2,
                                shell=True)
    data = json.loads(run)
    similarity = int(data[u'Similarity'])
    return similarity

def get_all_faces():
    faces = glob.glob("unknowfaces/*.jpg")
    for im1 in faces:
        for im2 in faces:
            f1_name = im1.split('/')[-1]
            f2_name = im2.split('/')[-1]

            r1_face = "@" + os.path.realpath(im1)
            r2_face = "@" + os.path.realpath(im2)
            res = curl(r1_face, r2_face)
            print('Similarity btwn {} and {} : {}'.format(f1_name, f2_name, res))

def main():
    get_all_faces()

if __name__ == '__main__':
    main()
