#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(file_new):
    fn = open(file_new, "rb")  # file_new是查找到的最新的测试报告的路径
    mail_body = fn.read()
    fn.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')  # MIMRText是python中一个支持html格式邮件的类，msg是MIMEText的一个实例化对象
    msg['Subject'] = Header('自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("gaowanru2016@126.com", "gao3901012")
    smtp.sendmail("gaowanru2016@126.com", "892342269@qq.com", msg.as_string())
    smtp.quit()
    print(" 邮件已成功发送！ ")


#  查找测试报告目录，找到最新的测试报告
def find_new_file(html_report_loc):  # html_report是存放测试报告的目录路径
    lists = os.listdir(html_report_loc)
    lists.sort(key=lambda fn: os.path.getmtime(html_report_loc+'\\'+fn))
    file_new = os.path.join(html_report_loc, lists[-1])
    return file_new
