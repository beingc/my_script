#!/usr/bin/env python3
# coding=utf-8
# Date: 2022/7/10
# Desc: remove duplicate lines

input_file = 'temp/track.txt'
output_file = 'temp/track2.txt'
list_1 = []

with open(input_file, 'r') as f:
    for line in f.readlines():
        if line.strip(' ') != '\n':
            list_1.append(line)

list_2 = list_1
print("Input line:", len(list_1))
try:
    for i in list(range(len(list_1))):
        for j in list(range(len(list_2))):
            if list_1[i] == list_2[j]:
                print(list_1[i])
                del list_1[i]
except IndexError:
    pass

print("Output line:", len(list_1))
with open(output_file, 'w') as f:
    f.writelines(list_1)
