# coding=utf8
# desc: calculate the request cost time by the log
# (记录时间相差秒级)

from datetime import datetime

"""
日志处理后的格式:
2023-08-01 00:00:05.108,abcd1234
2023-08-01 00:00:10.110,abcd1234
"""

InputFileName = 'input.log'
OutputFileName = 'output.csv'
LIST_1 = []

with open(InputFileName, 'r') as f:
    for line in f.readlines():
        time_str, trace_id = line.strip().split(',')
        LIST_1.append([trace_id, time_str])

for i in list(range(len(LIST_1))):
    trace_id_str, time_str1 = LIST_1[i]
    del LIST_1[i][0]
    for j in list(range(len(LIST_1))):
        if trace_id_str == LIST_1[j][0]:
            time_str2 = LIST_1[j][1]
            time_1 = datetime.strptime(time_str1, '%Y-%m-%d %H:%M:%S.%f')
            time_2 = datetime.strptime(time_str2, '%Y-%m-%d %H:%M:%S.%f')
            cost_time = (time_2 - time_1).seconds * 1000 + (time_2 - time_1).microseconds // 1000
            line_str = f"{trace_id_str},{time_str1},{time_str2},{cost_time}\n"
            with open(OutputFileName, 'a') as f:
                f.writelines(line_str)
