#!/usr/bin/env python3
# coding=utf-8
# Date: 2022/7/10
# Desc: remove duplicate lines

def deduplicate_lines(in_f, out_f):
    with open(in_f, 'r') as f:
        data = sorted(set(line.strip() for line in f))

    with open(out_f, 'w') as f:
        f.writelines(line + '\n' for line in data)


if __name__ == '__main__':
    input_file = 'temp/all_track.txt'
    output_file = 'temp/track.txt'
    deduplicate_lines(input_file, output_file)
