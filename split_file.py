# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:19:09 2018

@author: Joshua
"""
 # file name, extension, and max line count
def split_file(filename,ext, max_count):
    cnt = 0
    idx = 1

    file2 = open(filename + '_split_' + str(cnt) + '.csv', mode='w')
    
    # built in python function returns a file object
    with open(filename + '.' + ext, mode='r') as file:    
        for row in file:
            if (idx % max_count) == 0:
                cnt += 1
                file2.close()
                file2 = open(filename + '_split_' + str(cnt) + '.' + ext, mode='w')
            file2.write(row)
            idx += 1
    
    file.close()
    file2.close()

split_file('train', 'csv', 10 ** 7)