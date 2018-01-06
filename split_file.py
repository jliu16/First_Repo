# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:19:09 2018

@author: Joshua
"""
# splits file of rows into multiple files
# file name or directory, extension, and max line count
def split_file(filename, ext, max_count=10**3):
    file_cnt = 0
    idx = 1
    
    # built in python function returns a file object
    try:
        with open(filename + '.' + ext, mode='r') as myfile:
            write_file = open(filename + '_split_' + str(file_cnt) + '.csv', mode='w')
            
            for row in myfile:
                
                if (idx % max_count) == 0:
                    file_cnt += 1
                    write_file.close()
                    write_file = open(filename + '_split_' + str(file_cnt) + '.' + ext, mode='w')
                
                write_file.write(row)
                idx += 1
        
        myfile.close()
        write_file.close()
    except IOError:
        print('Could not find file:', filename + '.' + ext)

split_file('train', 'csv', 10 ** 7)