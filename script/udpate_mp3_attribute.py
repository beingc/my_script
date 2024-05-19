# coding=utf8
# Desc: batch update mp3 file attribute

import os
import eyed3

# 定义要更新的属性
album = "Your Album"
artist = "Your Name"
copyright = "Your Name"

# 指定包含 MP3 文件的文件夹路径
folder_path = "temp"

# 遍历文件夹下的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".mp3"):
        file_path = os.path.join(folder_path, file_name)

        # 加载 MP3 文件
        audiofile = eyed3.load(file_path)

        # 更新属性
        if audiofile.tag:
            audiofile.tag.album = album
            audiofile.tag.artist = artist
            audiofile.tag.copyright = copyright
            # 保存更改
            audiofile.tag.save()
            print(f"已更新文件 '{file_name}' 的属性.")
        else:
            print(f"文件 '{file_name}' 没有有效的 ID3 标签.")
