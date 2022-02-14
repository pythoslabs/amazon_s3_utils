# Created : 2019 Nov 16

# Functions
# 1. Downloads the file from S3 ( into a temp storage location './tmp_download/file_downloaded'
# Get file attribs


import pandas as pd
import os
# Import the custom s3 utils file
import s3_utils  # Custom package
import file_utils # Custom package
import soup_utils  # Custom package

EC2_TEMP_FOLDER_PATH = './tmp_download/'
EC2_TEMP_FILE_PATH = './tmp_download/tmp_dl_file'

f1 = s3_utils.s3_File()  # create a s3_utils object ( refer to the s3_utils.py file for debugging )

loc_list = ['root/.folder/SubFolder/documents/121/23gg/ssfafa',
            'root/.folder/SubFolder/documents/121/23gg/dffaer',
            'root/.folder/SubFolder/documents/121/23gg/sffarc'
            ]

try:
    for s3_filelocation in loc_list :
        s3_fname = file_utils.Fn_split_fpath_give_fileName(s3_filelocation)
        print(s3_filelocation)
        print("------------------")
        #print(s3_fname)
        f1.download(s3_filelocation, EC2_TEMP_FOLDER_PATH + s3_fname)
except Exception  as e1 :
    print(str(e1))


