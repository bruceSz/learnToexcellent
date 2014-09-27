#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import sys

def get_dir(path):
    print path,'\n'
    return os.listdir(path)

def bak_file(path,path_bak):
    list = os.listdir(path)
    for l in list:
        file_path = os.path.join(path,l)
        file_path_bak = os.path.join(path_bak,l)
        print file_path
        if os.path.isdir(file_path):
            if not os.path.isdir(file_path_bak):
                create_com = ''' mkdir -p '%s' ''' %(file_path_bak)
                if os.system(create_com) == 0:
                    print create_com
                else:
                    print 'create folder failure'
                    os._exit(0)
            bak_file(file_path,file_path_bak)

        

if __name__ == '__main__':
    
