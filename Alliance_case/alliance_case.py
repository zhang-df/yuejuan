# coding=utf-8
from 任务构建程序 import *
from 扫描上传程序 import *
from 分配任务程序 import *
from 接口评阅程序 import *
from 成绩相关程序 import *
from sha_ import *
from BeautifulReport import BeautifulReport
import unittest
import threading
import os
scale = 100


class AllianceCase(unittest.TestCase):

    def test_0(self):
        """执行开始程序"""
        sleep(1)
        print("执行开始，祈祷不报错".center(scale // 2, "-"))

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
        """接口评阅程序"""
        #   线程
        file = open('D:\PyCharm\projects\intranet\Alliance_case/user.txt', 'r', encoding='utf-8')
        next(file)
        with file as teachers:
            teachers = teachers.read().split('\n')
        for thread in teachers:
            t = threading.Thread(target=接口评阅程序, args=(thread,))
            t.setDaemon(True)
            t.start()
        t.join()

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
    suite.addTest(unittest.makeSuite(AllianceCase))
    run = BeautifulReport(suite)
    run.report(description='联盟测试报告',
               filename=u"YJ_report" + ".html",
               report_dir=os.path.join(os.getcwd(), "report"))
    Sha().send_email()
