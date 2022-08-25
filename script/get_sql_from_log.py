# coding=utf8
# desc: get sql from log

import re

LOG_TEXT = """
2022-08-25 18:18:18|ERROR|sql[select * from test t where t.a=? and t.b=? and t.c=?],parameters[a,null,{"c":"1","d":2}]
"""

SQL_TEXT = LOG_TEXT.split('[')[1].split(']')[0]
# 去除多余的空格（只保留一个）
SQL_TEXT = " ".join(SQL_TEXT.split())
PARAMS_TEXT = LOG_TEXT.split('[')[2].split(']')[0]
# 去除所有的空格
PARAMS_TEXT = "".join(PARAMS_TEXT.split())
SQL_PARAMS_NUM = len((re.findall(r'\?', SQL_TEXT)))
# 将"?"替换为"{}"且加上双引号
SQL_TEXT = re.sub(r'\?', r"'{}'", SQL_TEXT)
# 以","分割参数，不分割"{}"中的","
PARAMS_TEXT = re.split(r',(?![^{]*\})', PARAMS_TEXT)
PARAMS_LIST_NUM = len(PARAMS_TEXT)
# 分割的参数数量应该一致
assert SQL_PARAMS_NUM == PARAMS_LIST_NUM
# 拆解列表为参数（单*拆解列表，双*拆解字典）
SQL_TEXT = SQL_TEXT.format(*PARAMS_TEXT)
# 将"null"去掉引号
SQL_TEXT = re.sub(r"'null'", r'null', SQL_TEXT)
print(SQL_TEXT)
