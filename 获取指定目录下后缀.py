#! /usr/bin/python
# -*- coding: utf-8 -*-

import os


def getFileName(path):
    ''' ��ȡָ��Ŀ¼�µ�����ָ����׺���ļ��� '''

    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        # os.path.splitext():�����ļ�������չ��
        if os.path.splitext(i)[1] == '.log':
            print i


if __name__ == '__main__':

    path = '/home/xx/work/ETS/log/1/1'
    getFileName(path)