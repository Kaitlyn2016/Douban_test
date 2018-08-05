#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,json
import unittest
class Test(unittest.TestCase):
    url = "https://api.douban.com/v2/movie/search?"
    actor_name = "q=TomCruise"
    style_tag = "tag=爱情"
    name = "汤姆·克鲁斯"
    action = "动作"
    def setUp(self):
        # 初始化信息
        print("start!")

    def test_actor(self):
        # 执行测试
        req = requests.get(self.url + self.actor_name) # 通过requests 发起请求
        req = json.dumps(req.json(), ensure_ascii=False, indent=4)
        self.assertIn(self.name, req, msg=None) # 检查有没有 "汤姆·克鲁斯"这个演员

    def test_style_tag(self):
        # 执行测试
        req = requests.get(self.url + self.actor_name) # 通过requests 发起请求
        req = json.dumps(req.json(), ensure_ascii=False, indent=4)
        self.assertIn(self.action, req, msg=None) # 检查有没有 "动作片"