# coding=utf-8
# Create at: 2018/06/27
# Description: Get win10 lock screen wallpaper and save at 'D:\temp'

import os
import glob
import shutil
from datetime import datetime


def get_file_list(path):
    src_file_list = []
    for file in os.listdir(path):
        abs_path = os.path.join(path, file)
        # Remove file which size less then 200K
        if os.path.getsize(abs_path) > 204800:
            src_file_list.append(abs_path)
    return src_file_list


def copy_file(path_list, path):
    if not os.path.exists(path):
        os.mkdir(path)
    for file in path_list:
        shutil.copy(file, path)


def file_rename(path):
    now_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    count = 0
    for file in os.listdir(path):
        os.rename(os.path.join(path, file), os.path.join(path, str(now_time)+str(count)+".jpg"))
        count += 1
    print("Save %s picture files at %s" % (count, path))


if __name__ == '__main__':
    # Win10 lock screen wallpaper location
    src_path = glob.glob(r"C:\Users\x*\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")[0]
    # path to save the wallpaper
    dst_path = r"D:\temp"

    file_list = get_file_list(src_path)
    copy_file(file_list, dst_path)
    file_rename(dst_path)
    os.system('explorer.exe D:\\temp')
