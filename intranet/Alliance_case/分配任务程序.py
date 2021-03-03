# coding=utf-8
from def_ import *
import pyautogui
import pyperclip


def 分配任务程序():
    dr = Browser_()
    num = 1
    pyautogui.PAUSE = 1
    dr.open_("http://yjadmin.21cnjy.com:10192")
    sleep(2)
    dr.is_displayed('id', 'btn-login')
    dr.click_('id', 'btn-login')
    dr.input_('name', 'UserName', '11025688')
    dr.input_('name', 'Password', 'a123456')
    dr.click_('id', 'login-submit')

    # 任务分配
    sleep(2)
    dr.driver.switch_to.frame("main-frame")
    dr.is_displayed('xpath', '//a[text()="下一页"]')
    dr.click_('xpath', '(//label[contains(@onclick,"location")])[1]')
    dr.click_('xpath', '//a[text()="5.任务分配"]')
    dr.click_('xpath', '//div[text()="分配阅卷任务"]')
    dr.driver.switch_to.frame('(//iframe[@class="index-content"])[2]')

    # 语文科目教师导入
    dr.is_displayed('xpath', '//a[text()="如何进行题组调度?"]')
    dr.click_('id', 'btn-import')
    sleep(1)
    dr.mouse('id', 'file1')
    sleep(2)
    pyautogui.press('shift')
    pyperclip.copy(r'D:\PyCharm\File\Import\intranet\语文.xls')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(1)
    dr.click_('xpath', '//button[text()="导入"]')
    dr.is_displayed('xpath', '//div[text()="分配题组"]')
    sleep(1)
    dr.click_('xpath', '//a[text()="确认"]')
    sleep(2)
    dr.click_('xpath', '//span[text()="不限量-单评"]')
    sleep(2)

    # 数学科目教师导入
    dr.click_('xpath', '//a[text()="数学"]')
    dr.is_displayed('xpath', '//span[text()="数学"]')
    dr.click_('id', 'btn-import')
    sleep(1)
    dr.mouse('id', 'file1')
    sleep(2)
    pyautogui.press('shift')
    pyperclip.copy(r'D:\PyCharm\File\Import\intranet\数学.xls')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(1)
    dr.click_('xpath', '//button[text()="导入"]')
    dr.is_displayed('xpath', '//div[text()="分配题组"]')
    sleep(1)
    dr.click_('xpath', '//a[text()="确认"]')
    sleep(2)
    print('教师导入完毕')

    # 分配试卷
    while num <= 50:
        try:
            ele = dr.driver.find_element_by_xpath(
                '(//span[text()="350"])[2]').is_displayed()
            if ele is not None:
                break
        except Exception as e:
            sleep(10)
            dr.click_('xpath', '//span[text()="限量-单评"]')
            if num == 50:
                raise e
            num += 1
    sleep(0.5)
    dr.click_('id', 'btn-set-avg')
    dr.click_('xpath', '(//button[text()="提交"])[1]')
    sleep(1)
    dr.click_('xpath', '//a[text()="确定"]')
    sleep(3)
    num = 1
    while num <= 20:
        try:
            dr.driver.find_element_by_xpath(
                '(//span[text()="175"])[2]').is_displayed()
        except Exception as e:
            dr.click_('xpath', '//span[text()="限量-单评"]')
            if num == 20:
                raise e
            num += 1
        else:
            break
    dr.click_('xpath', '//span[text()="限量-双评"]')
    dr.is_displayed('xpath', '//span[text()="双评"]')
    dr.is_displayed('xpath', '(//label[contains(@title,"姓名")])[1]')
    sleep(0.5)
    dr.click_('id', 'btn-set-avg')
    dr.click_('xpath', '(//button[text()="提交"])[1]')
    sleep(1)
    dr.click_('xpath', '//a[text()="确定"]')
    sleep(3)
    num = 1
    while num <= 20:
        try:
            dr.driver.find_element_by_xpath(
                '(//span[text()="350"])[2]').is_displayed()
        except Exception as e:
            dr.click_('xpath', '//span[text()="限量-双评"]')
            if num == 20:
                raise e
            num += 1
        else:
            break
    dr.click_('xpath', '//span[text()="限量-二加一"]')
    dr.is_displayed('xpath', '//span[text()="2+1"]')
    dr.is_displayed('xpath', '(//label[contains(@title,"姓名")])[1]')
    sleep(0.5)
    dr.click_('id', 'btn-set-avg')
    dr.click_('xpath', '(//button[text()="提交"])[1]')
    sleep(1)
    dr.click_('xpath', '//a[text()="确定"]')
    sleep(3)
    num = 1
    while num <= 20:
        try:
            dr.driver.find_element_by_xpath(
                '(//span[text()="350"])[2]').is_displayed()
        except Exception as e:
            dr.click_('xpath', '//span[text()="限量-二加一"]')
            if num == 20:
                raise e
            num += 1
        else:
            break
    dr.click_('xpath', '//span[text()="限量-二加一加一"]')
    dr.is_displayed('xpath', '//span[text()="2+1+1"]')
    dr.input_(
        'xpath',
        '//label[text()="阅卷教师1"]/../input[1]',
        350)
    dr.input_(
        'xpath',
        '//label[text()="阅卷教师2"]/../input[1]',
        350)
    dr.click_('xpath', '(//button[text()="提交"])[1]')
    sleep(1)
    dr.click_('xpath', '//a[text()="确定"]')
    sleep(3)
    dr.click_('xpath', '//span[text()="限量-二加一加一"]')
    num = 1
    while num <= 20:
        try:
            dr.driver.find_element_by_xpath(
                '(//span[text()="350"])[2]').is_displayed()
        except Exception as e:
            sleep(2)
            dr.click_('xpath', '//span[text()="限量-二加一加一"]')
            if num == 20:
                raise e
            num += 1
        else:
            break
    print('试卷分配完毕')
    sleep(2)

    # 答卷扫描
    dr.driver.switch_to.parent_frame()
    num = 1
    while num <= 50:
        try:
            dr.click_('xpath', '//a[text()="7.答卷扫描"]')
            dr.driver.find_element_by_xpath('(//a[text()="开始正评"])[2]').is_displayed()
        except Exception as e:
            sleep(10)
            if num == 50:
                raise e
            num += 1
        else:
            break
    dr.click_('xpath', '(//a[text()="开始正评"])[2]')
    dr.click_('xpath', '(//a[text()="开始正评"])[1]')
    dr.is_displayed('xpath', '(//a[text()="正在评阅"])[2]')
    dr.driver.quit()
    print('任务开始正评')
