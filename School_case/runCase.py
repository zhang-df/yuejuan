# coding=utf-8
from testcase.任务构建程序 import *
from testcase.扫描上传程序 import *
from testcase.分配任务程序 import *
from testcase.评阅试卷程序 import *
from testcase.成绩相关程序 import *
from BeautifulReport import BeautifulReport
from utils.sha_ import *
from utils.def_ import *
import unittest
import os
scale = 100


class SchoolCase(unittest.TestCase):

    def test_0(self):
        """执行开始程序"""
        sleep(1)
        print("执行开始，祈祷不报错啊".center(scale // 2, "-"))

    def test_1(self):
        """任务构建程序"""
        任务构建程序()

    def test_2(self):
        """扫描上传程序"""
        扫描上传程序()

    def test_3(self):
        """分配任务程序"""
        分配任务程序()

    def test_4(self):
        """评阅试卷程序"""
        评阅试卷程序()

    def test_5(self):
        """成绩相关程序"""
        成绩相关程序()

    def test_End(self):
        """执行结束程序"""
        sleep(1)
        print("\n" + "执行结束，希望人有事".center(scale // 2, "-"))


if __name__ == '__main__':
    """测试任务"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SchoolCase))
    run = BeautifulReport(suite)
    run.report(description='校级测试报告',
               filename=u"BeautifulReport" + ".html",
               report_dir=os.path.join(os.getcwd(), "Report"))
    Sha().send_email()
