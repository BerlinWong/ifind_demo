#!/usr/local/anaconda3/envs
# -*- coding: utf-8 -*-
# @Time    : 2023/12/12 15:31
# @Author  : Berlin Wong
# @File    : demo.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

from iFinDPy import *
from datetime import datetime
import pandas as pd
import time as _time
import json
from threading import Thread, Lock, Semaphore
import requests

sem = Semaphore(5)  # 此变量用于控制最大并发数
dllock = Lock()  # 此变量用来控制实时行情推送中落数据到本地的锁


# 登录函数
def thslogindemo():
    # 输入用户的帐号和密码
    thsLogin = THS_iFinDLogin("username", "passwd")
    print(thsLogin)
    if thsLogin != 0:
        print('登录失败')
    else:
        print('登录成功')


def datapool_tick_demo():
    today_str = datetime.today().strftime('%Y-%m-%d')
    data_ss = THS_SS('RUZL.SHF', 'ms;tradeDate;tradeTime;latest;amt;vol;latestVolume;dealDirection;dealtype', '',
                     '2023-12-12 14:59:58', '2023-12-12 15:00:00')
    if data_ss.errorcode != 0:
        print('error:{}'.format(data_ss.errmsg))
    else:
        print(type(data_ss.data))
        data_df = data_ss.data
        data_df.to_csv(f'./data/demo{today_str}.csv', index=False)


def main():
    # 登录函数
    thslogindemo()
    datapool_tick_demo()


if __name__ == '__main__':
    main()
