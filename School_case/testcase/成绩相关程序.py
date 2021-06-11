# coding=utf-8
from utils.def_ import *
from utils.sha_ import user_


def 成绩相关程序():
    try:
        dr = Browser()
        #   登录进入二一阅卷
        dr.open_("http://yjadmin.21cnjy.com:10192")
        sleep(2)
        dr.is_displayed('id', 'btn-login')
        dr.click_('id', 'btn-login')
        dr.input_('name', 'UserName', user_('username'))
        dr.input_('name', 'Password', user_('password'))
        dr.click_('id', 'login-submit')

        #   进入考试任务
        sleep(2)
        dr.driver.switch_to.frame("main-frame")
        dr.is_displayed('xpath', '//a[text()="下一页"]')
        dr.click_('xpath', '(//label[contains(@onclick,"location")])[1]')

        #   成绩发布
        dr.click_('xpath', '//a[text()="10.成绩发布"]')
        dr.is_displayed('xpath', '//a[text()="发布全部科目"]')
        num = 1
        while num <= 250:
            '''不戳就是250'''
            try:
                dr.driver.find_element_by_xpath(
                    '//td[contains(text(), "1860")]').is_displayed()
                dr.driver.find_element_by_xpath(
                    '//td[contains(text(), "1250")]').is_displayed()
            except Exception as e:
                sleep(60)
                dr.click_('xpath', '//a[text()="10.成绩发布"]')
                if num == 250:
                    raise e
                num += 1
            else:
                break
        dr.click_('xpath', '(//a[text()="处理客观题"])[1]')
        dr.is_displayed('xpath', '//a[text()="如何进行异常处理?"]')
        sleep(1)
        num = 1
        while num <= 10:
            try:
                dr.click_('id', 'btn-save')
                dr.driver.find_element_by_xpath('//span[text()="保存成功"]').is_displayed()
            except Exception as e:
                if num == 10:
                    raise e
                else:
                    num += 1
            else:
                break
        sleep(3)
        dr.click_('xpath', '//a[text()="数学"]')
        dr.is_displayed('xpath', '//span[text()="0"]')
        sleep(1)
        while num <= 10:
            try:
                dr.click_('id', 'btn-save')
                dr.driver.find_element_by_xpath('//span[text()="保存成功"]').is_displayed()
            except Exception as e:
                if num == 10:
                    raise e
                else:
                    num += 1
            else:
                break
        sleep(3)
        dr.click_('xpath', '//a[text()="10.成绩发布"]')
        dr.is_displayed('xpath', '//a[text()="发布全部科目"]')
        # 取评分率
        scoring_rate1 = dr.driver.find_element_by_xpath(
            '//table/tbody/tr[2]/td[7]').text
        scoring_rate2 = dr.driver.find_element_by_xpath(
            '//table/tbody/tr[3]/td[7]').text
        num = 1
        while num <= 50:
            try:
                dr.click_('xpath', '(//a[text()="发　　布"])[1]')
                dr.driver.find_element_by_xpath('//div[text()="操作成功"]').is_displayed()
            except Exception as e:
                sleep(5)
                if num == 250:
                    raise e
                num += 1
            else:
                break
        num = 1
        while num <= 50:
            try:
                dr.driver.find_element_by_xpath(
                    '(//a[text()="重新发布"])[1]').is_displayed()
            except Exception as e:
                sleep(10)
                dr.click_('xpath', '//a[text()="10.成绩发布"]')
                dr.is_displayed('xpath', '//a[text()="如何发布及下发成绩?"]')
                if num == 50:
                    raise e
                num += 1
            else:
                break
        scoring_rate3 = dr.driver.find_element_by_xpath(
            '//table/tbody/tr[2]/td[7]').text
        num = 1
        while num <= 50:
            try:
                dr.click_('xpath', '(//a[text()="发　　布"])[1]')
                dr.driver.find_element_by_xpath('//div[text()="操作成功"]').is_displayed()
            except Exception as e:
                sleep(5)
                if num == 50:
                    raise e
                num += 1
            else:
                break
        num = 1
        while num <= 50:
            try:
                dr.driver.find_element_by_xpath(
                    '(//a[text()="重新发布"])[2]').is_displayed()
            except Exception as e:
                sleep(10)
                dr.click_('xpath', '//a[text()="10.成绩发布"]')
                dr.is_displayed('xpath', '//a[text()="如何发布及下发成绩?"]')
                if num == 50:
                    raise e
                num += 1
            else:
                break
        dr.click_('xpath', '//a[text()="10.成绩发布"]')
        sleep(1)
        scoring_rate4 = dr.driver.find_element_by_xpath(
            '//table/tbody/tr[3]/td[7]').text
        try:
            if scoring_rate1 == scoring_rate3:
                print('科目一评分率异常')
            if scoring_rate2 == scoring_rate4:
                print('科目二评分率异常')
            else:
                print('科目评分率正常')
        except Exception as e:
            print('科目评分率异常')
            raise e

        #   查看分数
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("index-container-left")
        sleep(1)
        dr.click_('xpath', '//span[text()="成绩分析"]')
        sleep(1)
        dr.click_('xpath', '//a[text()="成绩报告"]')
        sleep(1)
        dr.click_('xpath', '//a[text()="校级报告"]')
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("main-frame")
        sleep(1)
        dr.is_displayed('xpath', '(//a[text()="查看报告"])[1]')
        try:
            dr.driver.find_element_by_id('btn-fictitious').click()
        except Exception as e:
            raise e
        dr.click_('xpath', '(//a[text()="查看报告"])[1]')
        dr.is_displayed('id', 'fullscore')
        dr.click_('xpath', '//a[text()="学生成绩汇总"]')
        dr.input_('name', 'studentName', 'T1_0010')
        dr.click_('xpath', '//button[text()="搜索"]')
        dr.is_displayed('xpath', '//td[text()="T1_0010"]')
        sleep(1)
        initial1 = dr.driver.find_element_by_xpath('(//td)[8]').text
        dr.input_('name', 'studentName', 'T1_0020')
        dr.click_('xpath', '//button[text()="搜索"]')
        dr.is_displayed('xpath', '//td[text()="T1_0020"]')
        sleep(1)
        initial2 = dr.driver.find_element_by_xpath('(//td)[9]').text

        #   评分修正
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("index-container-left")
        dr.click_('xpath', '//span[text()="考试管理"]')
        sleep(0.5)
        dr.click_('xpath', '//a[text()="考试任务"]')
        sleep(2)
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("main-frame")
        dr.is_displayed('xpath', '//a[text()="下一页"]')
        dr.click_('xpath', '(//label[contains(@onclick,"location")])[1]')
        dr.click_('xpath', '//a[text()="9.异常处理"]')
        dr.click_('xpath', '//a[text()="评分修正"]')
        dr.is_displayed('css', '[data-code="24"]')
        dr.input_('name', 'testCode', '210118010')
        dr.input_('name', 'studentName', 'T1_0010')
        dr.click_('css', '[value="搜索"]')
        dr.is_displayed('xpath', '//em[text()="T1_0010"]')
        dr.driver.find_element_by_xpath(
            '//span[text()="1.1"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.2"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.3"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.4"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.5"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.6"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.7"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.8"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.9"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.10"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.11"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.12"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.13"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.14"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.15"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.16"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.17"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.18"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.19"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.20"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.1"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.2"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.3"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.4"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.5"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.6~3.10 "]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="4.11~4.13 | 4.15 "]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="4.14(1~2) | 4.14(5~6) "]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="4.14(3~4) "]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="5.16"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="6.17"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="7.18(附)"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="7.19(附)"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="7.20(附)"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="7.21(附)"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="7.22(附)"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="7.23(附)"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="7.24~7.27 (附)"]').is_displayed()
        sleep(1)
        score = dr.driver.find_element_by_xpath(
            '(//em[contains(@class-,"dj-current")])[7]').text
        full_score1 = dr.driver.find_element_by_xpath(
            '(//em[contains(@class,"dj-total")])[7]').text
        objective1 = dr.driver.find_element_by_xpath('(//a[@class="active"])[2]').text
        ele = dr.driver.find_element_by_xpath('//span[text()="1.1"]')
        chain = ActionChains(dr.driver)
        chain.move_to_element(ele).perform()
        try:
            if objective1 == 'A':
                dr.click_('xpath', '(//a[@class="active"])[2]')
                dr.click_('xpath', '(//a[text()="B"])[1]')
            else:
                dr.click_('xpath', '(//a[@class="active"])[2]')
                dr.click_('xpath', '(//a[text()="A"])[1]')
        except Exception as e:
            raise e
        dr.js_('xpath', '//span[text()="7.18(附)"]')
        try:
            if score == full_score1:
                dr.input_(
                    'xpath',
                    '//*[@data-code="24"]/div/div/span[2]/input',
                    0)
                dr.click_('xpath', '//button[text()="确定修改"]')
                dr.is_displayed('xpath', '//span[text()="操作成功"]')
            else:
                dr.input_(
                    'xpath',
                    '//*[@data-code="24"]/div/div/span[2]/input',
                    full_score1)
                dr.click_('xpath', '//button[text()="确定修改"]')
                dr.is_displayed('xpath', '//span[text()="操作成功"]')
        except Exception as e:
            print('语文评分修正分数错误')
            raise e
        sleep(4)
        dr.select_('text', 'id', 'examSubject', '数学')
        dr.input_('name', 'testCode', '210118020')
        dr.input_('name', 'studentName', 'T1_0020')
        dr.click_('css', '[value="搜索"]')
        dr.is_displayed('xpath', '//em[text()="T1_0020"]')
        dr.driver.find_element_by_xpath(
            '//span[text()="1.1"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.2"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.3"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.4"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="1.5"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.6"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.7"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.8"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.9"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="2.10"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.11"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.12"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.13"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.14"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.15"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.16"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.17"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.18"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.19"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.20"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.21"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.22"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.23"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.24"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="3.25"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="4.26~4.28 "]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="5.29~5.31 "]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="5.32~5.33 "]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="5.34"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="5.35"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="6.36"]').is_displayed()
        dr.driver.find_element_by_xpath(
            '//span[text()="6.37"]').is_displayed()
        sleep(1)
        score = dr.driver.find_element_by_xpath(
            '(//em[contains(@class-,"dj-current")])[7]').text
        full_score2 = dr.driver.find_element_by_xpath(
            '(//em[contains(@class,"dj-total")])[7]').text
        objective2 = dr.driver.find_element_by_xpath('(//a[@class="active"])[2]').text
        ele = dr.driver.find_element_by_xpath('//span[text()="1.1"]')
        chain = ActionChains(dr.driver)
        chain.move_to_element(ele).perform()
        try:
            if objective2 == 'A':
                dr.click_('xpath', '(//a[@class="active"])[2]')
                dr.click_('xpath', '(//a[text()="B"])[1]')
            else:
                dr.click_('xpath', '(//a[@class="active"])[2]')
                dr.click_('xpath', '(//a[text()="A"])[1]')
        except Exception as e:
            print('评分修正答案错误')
            raise e
        dr.js_('xpath', '//span[text()="6.37"]')
        try:
            if score == full_score2:
                dr.input_(
                    'xpath',
                    '(//*[@data-code="22"])[3]/div/div/span/input',
                    0)
                dr.click_('xpath', '//button[text()="确定修改"]')
                dr.is_displayed('xpath', '//span[text()="操作成功"]')
            else:
                dr.input_(
                    'xpath',
                    '(//*[@data-code="22"])[3]/div/div/span/input',
                    full_score2)
                dr.click_('xpath', '//button[text()="确定修改"]')
                dr.is_displayed('xpath', '//span[text()="操作成功"]')
        except Exception as e:
            print('数学评分修正分数错误')
            raise e
        else:
            sleep(4)
            dr.click_('xpath', '//a[text()="修正记录"]')
            dr.is_displayed('xpath', '(//td[text()="210118010"])[1]')
            dr.is_displayed('xpath', '(//td[text()="210118010"])[2]')
            sleep(1)
            dr.select_('text', 'id', 'examSubject', '数学')
            dr.click_('css', '[value="搜索"]')
            dr.is_displayed('xpath', '(//td[text()="210118020"])[1]')
            dr.is_displayed('xpath', '(//td[text()="210118020"])[2]')
            sleep(2)
            print("评分修正正常")

        dr.click_('xpath', '//a[text()="10.成绩发布"]')
        dr.is_displayed('xpath', '//a[text()="发布全部科目"]')
        sleep(1)
        num = 1
        while num <= 20:
            try:
                dr.click_('xpath', '//a[text()="发布全部科目"]')
                dr.driver.find_element_by_xpath(
                    '//div[text()="操作成功"]').is_displayed()
            except Exception as e:
                if num == 20:
                    print('重新发布成绩错误')
                    raise e
            else:
                break
        sleep(5)
        dr.click_('xpath', '//a[text()="10.成绩发布"]')
        num = 1
        while num <= 20:
            try:
                dr.driver.find_element_by_xpath(
                    '(//a[text()="重新发布"])[1]').is_displayed()
                dr.driver.find_element_by_xpath(
                    '(//a[text()="重新发布"])[2]').is_displayed()
            except Exception as e:
                sleep(2)
                dr.click_('xpath', '//a[text()="10.成绩发布"]')
                if num == 20:
                    print('重新发布成绩错误')
                    raise e
                num += 1
            else:
                break
        sleep(2)

        # 报表生成
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("index-container-left")
        dr.click_('xpath', '//span[text()="成绩分析"]')
        sleep(1)
        dr.click_('xpath', '//a[text()="报表分析"]')
        dr.driver.switch_to.default_content()

        dr.driver.switch_to.frame("main-frame")
        dr.is_displayed('id', 'task_chosen')
        dr.click_('id', 'task_chosen')
        dr.click_('xpath', '(//li[text()="校级任务2021年04月23日 09-23-44"])')

        dr.click_('xpath', '//a[text()="确定"]')
        sleep(0.5)
        dr.click_('xpath', '(//a[text()="生成报表"])[3]')
        sleep(0.5)
        dr.click_('xpath', '//a[text()="确定"]')
        sleep(0.5)
        dr.click_('xpath', '(//a[text()="生成报表"])[2]')
        sleep(0.5)
        dr.click_('xpath', '//a[text()="确定"]')
        sleep(0.5)
        dr.click_('xpath', '(//a[text()="生成报表"])[1]')
        sleep(0.5)
        dr.click_('xpath', '//a[text()="确定"]')
        sleep(0.5)
        # num = 1
        # while num <= 20:
        #     try:
        #         dr.driver.find_element_by_xpath('(//a[text()="下载报表"])[1]').is_displayed()
        #         dr.driver.find_element_by_xpath('(//a[text()="下载报表"])[2]').is_displayed()
        #         dr.driver.find_element_by_xpath('(//a[text()="下载报表"])[3]').is_displayed()
        #         dr.driver.find_element_by_xpath('(//a[text()="下载报表"])[4]').is_displayed()
        #         dr.driver.find_element_by_xpath('(//a[text()="下载报表"])[5]').is_displayed()
        #     except Exception as e:
        #         sleep(5)
        #         if num == 20:
        #             print('报表生成错误')
        #             raise e
        #         num += 1
        #     else:
        #         print("报表生成成功")
        #         break
        # sleep(1)

        list = dr.driver.find_elements_by_xpath('(//a[text()="下载报表"])')
        for index in range(len(list)):
            try:
                dr.driver.find_element_by_xpath('(//a[text()="下载报表"])['+str(index+1)+']').click()
            except Exception as e:
                    print('报表生成错误')
                    raise e
            if index == len(list)-1:
                print('报表生成成功')
                break
        sleep(1)
        #   报告查看
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("index-container-left")
        sleep(1)
        dr.click_('xpath', '//a[text()="成绩报告"]')
        sleep(1)
        dr.click_('xpath', '//a[text()="校级报告"]')
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("main-frame")
        sleep(2)
        dr.is_displayed('xpath', '(//a[text()="查看报告"])[1]')
        dr.click_('xpath', '(//a[text()="查看报告"])[1]')
        dr.is_displayed('id', 'fullscore')
        dr.click_('xpath', '//a[text()="学生成绩汇总"]')
        dr.input_('name', 'studentName', 'T1_0010')
        dr.click_('xpath', '//button[text()="搜索"]')
        dr.is_displayed('xpath', '//td[text()="T1_0010"]')
        sleep(2)
        result1 = dr.driver.find_element_by_xpath('(//td)[8]').text
        dr.input_('name', 'studentName', 'T1_0020')
        dr.click_('xpath', '//button[text()="搜索"]')
        dr.is_displayed('xpath', '//td[text()="T1_0020"]')
        sleep(2)
        result2 = dr.driver.find_element_by_xpath('(//td)[9]').text
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("index-container-left")
        dr.click_('xpath', '//a[text()="班级报告"]')
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("main-frame")
        sleep(2)
        dr.is_displayed('xpath', '(//a[text()="查看报告"])[1]')
        try:
            dr.is_displayed('id', 'btn-fictitious')
            dr.driver.find_element_by_id('btn-fictitious').click()
        except Exception as e:
            raise e
        dr.click_('xpath', '(//a[text()="查看报告"])[1]')
        dr.is_displayed('id', 'chart-class-score')
        dr.click_('xpath', '//a[text()="成绩明细"]')
        dr.input_('name', 'studentName', 'T1_0010')
        dr.click_('xpath', '//button[text()="搜索"]')
        dr.is_displayed('xpath', '//td[text()="T1_0010"]')
        sleep(1)
        try:
            if initial1 != result1 and initial2 != result2:
                print('成绩报告分数正常')
            else:
                print('成绩报告分数异常')
        except Exception as e:
            print('成绩报告分数异常')
            raise e

        #  精准讲评
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("index-container-left")
        sleep(1)
        dr.click_('xpath', '//a[text()="精准讲评"]')
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("main-frame")
        dr.is_displayed('xpath', '(//div[@class="list-right"])[1]')
        dr.click_('xpath', '(//div[@class="list-right"])[1]')
        sleep(2)
        num = 1
        while num <= 20:
            try:
                dr.driver.find_element_by_xpath(
                    '//h2[@class="ecaluation-tit"]').is_displayed()
            except Exception as e:
                dr.driver.refresh()
                dr.driver.switch_to.frame("main-frame")
                dr.is_displayed('xpath', '(//div[@class="list-right"])[1]')
                dr.click_('xpath', '(//div[@class="list-right"])[1]')
                sleep(10)
                if num == 20:
                    raise e
                num += 1
            else:
                break
        try:
            average1 = dr.driver.find_element_by_xpath(
                '(//div[@class="evaluation-item"]/p)[1]').is_displayed()
            if average1 == '0':
                print('科目一精准讲评平均分错误')
                result3 = 'False'
            else:
                result3 = 'True'
        except Exception as e:
            result3 = 'False'
            print(e)
        try:
            knowledge1 = dr.driver.find_element_by_xpath(
                '(//div[@class="evaluation-knowledge-tit"])[10]').text
            if knowledge1 != '5.gkh':
                print('科目一精准讲评知识点错误')
                result4 = 'False'
            else:
                result4 = 'True'
        except Exception as e:
            result4 = 'False'
            print(e)
        try:
            dr.driver.find_element_by_xpath(
                '//a[text()="1.1"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.2"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.3"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.4"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.5"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.6"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.7"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.8"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.9"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.10"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.11"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.12"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.13"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.14"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.15"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.16"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.17"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.18"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.19"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.20"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.1"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.2"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.3"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.4"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.5"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.6~3.10 "]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="4.11~4.13 | 4.15 "]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="4.14(1~2) | 4.14(5~6) "]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="4.14(3~4) "]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="5.16"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="6.17"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="7.18"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="7.19"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="7.20"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="7.21"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="7.22"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="7.23"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="7.24~7.27 "]').is_displayed()
        except Exception as e:
            result5 = 'False'
            print('科目一精准讲评题号错误')
            print(e)
        else:
            result5 = 'True'
        try:
            if result3 == 'True' and result4 == 'True' and result5 == 'True':
                print('科目一精准讲评正常')
            else:
                print('科目一精准讲评出错')
        except Exception as e:
            print('科目一精准讲评出错')
            raise e
        sleep(2)
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("index-container-left")
        dr.click_('xpath', '//a[text()="精准讲评"]')
        dr.driver.switch_to.default_content()
        dr.driver.switch_to.frame("main-frame")
        dr.is_displayed('xpath', '(//div[@class="list-right"])[1]')
        dr.click_('xpath', '(//div[@class="list-right"])[2]')
        sleep(2)
        num = 1
        while num <= 20:
            try:
                dr.driver.find_element_by_xpath(
                    '//h2[@class="ecaluation-tit"]').is_displayed()
            except Exception as e:
                dr.driver.refresh()
                dr.driver.switch_to.frame("main-frame")
                dr.is_displayed('xpath', '(//div[@class="list-right"])[1]')
                dr.click_('xpath', '(//div[@class="list-right"])[2]')
                sleep(10)
                if num == 20:
                    raise e
                num += 1
            else:
                break
        try:
            average2 = dr.driver.find_element_by_xpath(
                '(//div[@class="evaluation-item"]/p)[1]').is_displayed()
            if average2 == '0':
                print('科目二精准讲评平均分错误')
                result6 = 'False'
            else:
                result6 = 'True'
        except Exception as e:
            result6 = 'False'
            print(e)
        try:
            knowledge2 = dr.driver.find_element_by_xpath(
                '(//div[@class="evaluation-knowledge-tit"])[54]').text
            if knowledge2 != '1.1～5的认识与读写':
                print('科目二精准讲评知识点错误')
                result7 = 'False'
            else:
                result7 = 'True'
        except Exception as e:
            result7 = 'False'
            print(e)
        try:
            dr.driver.find_element_by_xpath(
                '//a[text()="1.1"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.2"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.3"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.4"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="1.5"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.6"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.7"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.8"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.9"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="2.10"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.11"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.12"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.13"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.14"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.15"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.16"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.17"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.18"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.19"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.20"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.21"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.22"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.23"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.24"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="3.25"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="4.26~4.28 "]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="5.29~5.31 "]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="5.32~5.33 "]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="5.34"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="5.35"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="6.36"]').is_displayed()
            dr.driver.find_element_by_xpath(
                '//a[text()="6.37"]').is_displayed()
        except Exception as e:
            result8 = 'False'
            print('科目二精准讲评题号错误')
            print(e)
        else:
            result8 = 'True'
        try:
            dr.driver.find_element_by_xpath(
                '(//div[@class="evaluation-ques-tit"])[37]').is_displayed()
        except Exception as e:
            result9 = 'False'
            print('科目二精准讲评题干错误')
            print(e)
        else:
            result9 = 'True'
        try:
            dr.driver.find_element_by_xpath(
                '(//div[@class="evaluation-expand"])[26]').is_displayed()
        except Exception as e:
            result10 = 'False'
            print('科目二精准讲评解析错误')
            print(e)
        else:
            result10 = 'True'
        try:
            if result6 == 'True' and result7 == 'True' and result8 == 'True' and result9 == 'True' and result10 == 'True':
                print('科目二精准讲评正常')
            else:
                print('科目二精准讲评出错')
        except Exception as e:
            print('科目二精准讲评出错')
            raise e
        sleep(2)
        dr.driver.quit()
    except Exception as e:
        Browser().shot()
        raise e


if __name__ == '__main__':
    成绩相关程序()
