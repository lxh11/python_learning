# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:38:10 2019

@author: zsk11
"""
# batch_file_rename.py

# This will batch rename a group of files in a given directory 

# just checking
_author_='zsk'
_version_='1.0'

import os
import argparse 

def batch_rename (work_dir, old_ext, new_ext):
    # files=os.listddir(work_dir)
    for filename in os.listdir(work_dir):
        # get the file extension
        split_file=os.path.splitext(filename)
        file_ext=split_file[1]
        if old_ext==file_ext:
            # returns changed name of file extensions, if old_ext=file_ext
            newfile = split_file[0]+new_ext
            
            #write the files
            os.rename(
                    os.path.join(work_dir,filename),
                    os.path.join(work_dir,newfile)
            )
            
def get_parser():
    parser =argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1,help='the directory where to change extension')
    parser.add_argument('old_ext',metavar='OLD_EXT',type=str,nargs=1,help='old extension')
    parser.add_argument('new_ext',metavar='NEW_EXT',type=str,nargs=1,help='new extension')
    return parser

def main():
    parser=get_parser()
    args=vars(parser.parse_args())
    
    work_dir=args['work_dir'][0]
    old_ext=args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext='.'+old_ext
    new_ext=args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext='.'+new_ext
    batch_rename(work_dir,old_ext,new_ext)
    
if __name__ == '__main__':
    work_dir='C:/Users/zsk11/Downloads/svjour-spr-chicago'
    old_ext='.txt'
    new_ext='.txt'
    main()
    



