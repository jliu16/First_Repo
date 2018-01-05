# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:19:09 2018

@author: Joshua
"""

current_id = ''
index = 0
written_lines = 0
max_lines = 1000000

with open('data.csv', 'r') as input_file:
    for line in input_file:
        values = line.split(',')
        if (current_id != values[0]) or (written_lines > max_lines):
            index += 1
            current_id = values[0]
        with open('output_{:08d}.csv'.format(index), 'a') as output_file:
            output_file.write(line)
            written_lines += 1