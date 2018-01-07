# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:19:09 2018

@author: Joshua
"""

# splits file of rows into multiple files
# file name or directory, extension, and file size in bytes
def split_file(filename, ext, size=2 ** 28, newline='\n'):
    new_filename = filename + '_split_'
    file_cnt = 0
    tmp = ''
    
    # open is a built-in python function that returns a file object
    with open(filename + '.' + ext, mode='r') as myfile:        
        
        data = myfile.read(size)
        while (data != ''):
            
            idx = find_newline(data, newline)
            
            with open(new_filename + str(file_cnt) + '.' + ext, mode='w') as new_file:
                new_file.write(tmp + data[:idx+1])

            tmp = data[idx+1:]
            data = myfile.read(size)
            file_cnt += 1

# returns the index of the last new line character
def find_newline(text, newline='\n'):
    index = len(text)
    found = False
    while(not found and index > -1):
        index -= 1
        found = text[index] == newline
    return index

split_file('train', 'csv', size=2 ** 28)