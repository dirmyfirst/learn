#! /usr/bin/python
# -*- coding: utf-8 -*-

import os


def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''

    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.log':
            print i


if __name__ == '__main__':

    path = '/home/xx/work/ETS/log/1/1'
    getFileName(path)