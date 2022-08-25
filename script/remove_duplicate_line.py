#!/usr/bin/env python3
# coding=utf-8
# Date: 2022/7/10
# Desc: remove duplicate lines

input_file = 'temp/all_track.txt'
output_file = 'temp/track.txt'

list_1 = []
with open(input_file, 'r') as f:
    for line in f.readlines():
        if line.strip(' ') != '\n':
            list_1.append(line)
print("Input line:", len(list_1))

# 利用set去重
with open(output_file, 'w') as f:
    # for i in set(list_1):
    f.writelines(set(list_1))
print("Output line:", len(set(list_1)))
