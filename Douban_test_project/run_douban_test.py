#!/usr/bin/env python
# -*- coding: utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
import time
import unittest
from function import send_email, find_new_file


if __name__ == '__main__':
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # html存放文件路径
    file_name = './report/' + now + 'result.html'
    # 打开一个文件，将result写入此file中
    file = open(file_name, "wb")
    runner = HTMLTestRunner(stream=file, title='接口测试报告：', description='用例执行情况：')
    discover = unittest.defaultTestLoader.discover('./test_case', pattern='*_sta.py')
    # 这里填写你的测试用例名
    runner.run(discover)
    file.close()
    fnf = find_new_file('./report/')
    send_email(fnf)