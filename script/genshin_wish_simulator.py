# coding=utf8

import random

five_star_flag = 0
four_star_flag = 0


def make_a_wish():
    global five_star_flag
    global four_star_flag

    one_wish = random.random()
    five_star_flag += 1
    four_star_flag += 1
    # 5星角色祈愿的基础出率为0.600%
    if one_wish < 0.006:
        print(f"\033[33m5星\033[0m {five_star_flag}抽")
        five_star_flag = 0
    # 4星角色祈愿的基础出率为5.100%
    elif one_wish < 0.051:
        print(f"\033[34m4星\033[0m {four_star_flag}抽")
        four_star_flag = 0
    else:
        if five_star_flag >= 90:
            print(f"\033[33m5星\033[0m {five_star_flag} 保底")
            five_star_flag = 0
        elif four_star_flag >= 10:
            print(f"\033[34m4星\033[0m {four_star_flag} 保底")
            four_star_flag = 0
        else:
            print("垃圾")


def main(n):
    for i in range(n):
        make_a_wish()


if __name__ == '__main__':
    wish_times = 100
    main(wish_times)
