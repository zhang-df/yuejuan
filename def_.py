# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from time import *
import time
import datetime


class Browser_():
    # 定义浏览器的构造函数
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # 循环等待获取元素

    def get_position(self, method, value, timeout=10):
        driver = self.driver
        try:
            if method == "id":
                ele = WebDriverWait(driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.ID, value)))
            elif method == "name":
                ele = WebDriverWait(driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.NAME, value)))
            elif method == "xpath":
                ele = WebDriverWait(driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.XPATH, value)))
            elif method == "class":
                ele = WebDriverWait(driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, value)))
            elif method == "css":
                ele = WebDriverWait(driver, timeout, 1).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, value)))
            else:
                print('你输入了啥?')
        except Exception:
            # 元素没有找到自动截图
            self.shot()
        else:
            return ele

        # 判断元素是否出现

    def is_displayed(self, method, value):
        driver = self.driver
        num = 1
        while num <= 20:
            try:
                if method == 'id':
                    Resulf = driver.find_element_by_id(value).is_displayed()
                elif method == 'name':
                    Resulf = driver.find_element_by_name(value).is_displayed()
                elif method == 'xpath':
                    Resulf = driver.find_element_by_xpath(value).is_displayed()
                elif method == 'class':
                    Resulf = driver.find_element_by_class_name(
                        value).is_displayed()
                elif method == 'css':
                    Resulf = driver.find_element_by_css_selector(
                        value).is_displayed()
                if Resulf:
                    break
            except BaseException:
                sleep(1)
                num += 1

        # 打开浏览器

    def open_(self, url):
        self.driver.implicitly_wait(10)
        self.driver.get(url)

        # driver点击

    def click_(self, method, value):
        ele = self.get_position(method, value)
        if ele is not None:
            ele.click()
        else:
            print("driver点击错误")

        # driver输入

    def input_(self, method, value, data):
        ele = self.get_position(method, value)
        if ele is not None:
            ele.clear()
            ele.send_keys(data)
        else:
            print("driver输入错误")

        # 鼠标点击

    def mouse(self, method, value):
        ele = self.get_position(method, value)
        action = ActionChains(self.driver)
        if ele is not None:
            action.click(ele)
            action.perform()
        else:
            print("鼠标点击错误")

        # 键盘输入

    def mouse_(self, method, value, data):
        ele = self.get_position(method, value)
        action = ActionChains(self.driver)
        if ele is not None:
            action.send_keys(data)
            action.perform()
        else:
            print("键盘输入错误")

        # 鼠标双击

    def double_click(self, method, value):
        ele = self.get_position(method, value)
        action = ActionChains(self.driver)
        if ele is not None:
            action.double_click(ele)
            action.perform()
        else:
            print("键盘双击错误")

        # 使用js将页面滚到元素位置

    def js_(self, method, value):
        target = self.driver.find_element(method, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        # 使用js将页面滚到底部

    def executejs_(self):
        self.driver.execute_script(
            'var q=document.documentElement.scrollTop=10000')

        # 页面窗口切换

    def handles_(self, value):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[value])

        # 下拉框选取

    def Select_(self, means, method, value, data):
        try:
            if means == "value":
                Select(self.get_position(
                    method, value)).select_by_value(
                    data)
            if means == "index":
                Select(self.get_position(
                    method, value)).select_by_index(
                    data)
            if means == "text":
                Select(self.get_position(
                    method, value)).select_by_visible_text(
                    data)
            else:
                print()
        except BaseException:
            print('下拉框定位失败')

        # 等待时间

    def sleep(self, value):
        time.sleep(value)

        # driver截图

    def shot(self):
        t = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        self.driver.get_screenshot_as_file(
            r"D:\PyCharm\File\printscreen/%s.png" % t)