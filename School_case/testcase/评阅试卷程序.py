# coding=utf-8
from utils.def_ import *
import random


def initial_(dr, group, interface=None):
    """
    :param dr: driver
    :param group: 题组序号
    :param interface: 问题卷 or 三评卷 or 仲裁卷
    :return: initial
    """
    # 点击阅卷任务列表的第x个
    dr.click_('xpath', "(//a[text()='进行阅卷'])[%s]" % group)
    dr.handles_(-1)
    num = 1
    while True:
        try:
            element = dr.driver.find_elements_by_css_selector(
                '[style="margin: auto; display: none;"]')
            if element != []:
                initial = ''
                return initial
            else:
                print("弹出评阅完成窗口")
                pop_up = dr.driver.find_element_by_xpath(
                    '//a[text()="确定"]').is_displayed()
                if pop_up is not None:
                    num += 1
                    if num > 20:
                        dr.shot()
                        initial = 'Exception'
                        return initial
                    else:
                        sleep(5)
                        dr.click_('xpath', '//a[text()="确定"]')
                        dr.handles_(0)
                        dr.driver.refresh()
                        if interface:
                            dr.click_('xpath', '//div[text()="网上阅卷"]')
                            sleep(0.5)
                            dr.click_(
                                'xpath', '//div[text()="%s处理"]' %
                                interface)
                            dr.driver.switch_to.frame("//iframe")
                            dr.click_(
                                'xpath',
                                "(//a[text()='进行阅卷'])[%s]" %
                                group)
                            dr.handles_(-1)
                        else:
                            dr.driver.switch_to.frame("//iframe")
                            dr.click_(
                                'xpath',
                                "(//a[text()='进行阅卷'])[%s]" %
                                group)
                            dr.handles_(-1)
        except Exception as e:
            dr.shot()
            raise e


def online_marking(dr, pattern, question=None):
    """
    :param dr: driver
    :param pattern: 限量 or 不限量
    :param question: 问题卷数量上限
    :return: ''
    """

    if question:
        question = random.randint(0, question)

        if pattern == 'Not limited':
            amount = int(dr.driver.find_element_by_id("QGAllCount").text) / 2\
                - int(question)
        elif pattern == 'limited':
            amount = int(dr.driver.find_element_by_id(
                "IAllotCount").text) - int(question)

        for i in range(question):
            dr.click_('xpath', '//a[text()="设为问题卷"]')
            dr.is_displayed('xpath', '//a[text()="确定"]')
            sleep(0.5)
            dr.click_('xpath', '//a[text()="确定"]')
            dr.is_displayed('xpath', '//div[text()="操作成功"]')
            sleep(1)

    else:
        if pattern == 'Not limited':
            done = int(dr.driver.find_element_by_id("QGReadCount").text)
            amount = int(dr.driver.find_element_by_id(
                "QGAllCount").text) - done
        elif pattern == 'limited':
            done = int(dr.driver.find_element_by_id("IReadCount").text)
            amount = int(dr.driver.find_element_by_id(
                "IAllotCount").text) - done

    interface = dr.driver.find_element_by_xpath(
        '//h3[@class="panel-title"]/label').text
    topic_number = get_topic(dr)
    num = 0

    while True:
        try:
            for i in range(len(topic_number)):
                data = random.randint(0, topic_number[i])
                dr.input_(
                    'xpath', '(//input[contains(@name,"score")])[{}]'.format(i + 1), data)
            dr.click_('xpath', "//button[text()='提交']")
            num += 1
            if num >= amount:
                pop_up = dr.driver.find_element_by_xpath(
                    "//a[text()='确定']")
                sleep(2)
                if pop_up:
                    dr.click_('xpath', "//a[text()='确定']")
                    dr.handles_(0)
                    return ''
                else:
                    if num > amount:
                        dr.shot()
                        print('题组一提交评阅异常')
                        return 'Exception'
            else:
                if interface != '问题卷':
                    dr.is_displayed('xpath', '//div[text()="操作成功"]')
                    sleep(1)
                else:
                    dr.is_displayed('xpath', '//div[text()="评阅成功"]')
                    sleep(1)
        except Exception as e:
            if pattern == 'Not limited':
                done = int(dr.driver.find_element_by_id("QGReadCount").text)
                if done >= amount:
                    dr.click_('xpath', '//button[text()="关闭"]')
                    sleep(0.5)
                    dr.click_('xpath', "//a[text()='确定']")
                    dr.handles_(0)
                    return ''
                else:
                    raise e
            else:
                raise e


def get_topic(dr) -> list:
    """
    :param dr: driver
    :return: topic_list
    """

    topic_list = []
    topic_number = dr.driver.find_elements_by_xpath('//em')
    for i in range(len(topic_number)):
        topic = int(dr.driver.find_element_by_xpath(
            '(//em)[{}]'.format(i + 1)).text)
        topic_list.append(topic)
    return topic_list


def get_group(dr, interface=None) -> list:
    """
    :param dr: driver
    :param interface: 问题卷 or 三评卷 or 仲裁卷
    :return: group_list
    """

    if interface:
        dr.click_('xpath', '//div[text()="网上阅卷"]')
        sleep(0.5)
        dr.click_('xpath', '//div[text()="%s处理"]' % interface)
        dr.driver.switch_to.frame("//iframe")
        dr.is_displayed('xpath', '//a[text()="如何处理%s?"]' % interface)
    else:
        dr.driver.switch_to.frame("//iframe")
        dr.is_displayed('xpath', '//a[text()="如何进行网上阅卷?"]')
    group_list = dr.driver.find_elements_by_xpath(
        '//ul[@class="list-task list-task-hidden"]/li')
    dr.driver.switch_to.parent_frame()
    return group_list


def get_pattern(dr, group, interface=None):
    """
    :param dr: driver
    :param group: 题组序号
    :param interface:  问题卷 or 三评卷 or 仲裁卷
    :return: group_pattern
    """
    if interface:
        dr.click_('xpath', '//div[text()="网上阅卷"]')
        sleep(0.5)
        dr.click_('xpath', '//div[text()="%s处理"]' % interface)
        dr.driver.switch_to.frame('//iframe')
        dr.is_displayed('xpath', '//a[text()="如何处理%s?"]' % interface)
        return 'Not limited'
    else:
        dr.driver.switch_to.frame('//iframe')
        group_pattern = dr.driver.find_element_by_xpath(
            '(//div[@class="list-info-item "]/span)[%s]' % group).text
        if group_pattern == '模式：限量':
            return 'limited'
        else:
            return 'Not limited'


def 评阅试卷程序():
    try:
        yj1, yj2, yj3 = '阅卷教师1', '阅卷教师2', '阅卷教师3'  # 评阅账号
        question = random.randint(1, 5)
        result_ = ''

        #    登录界面
        dr = Browser()
        dr.driver.get("http://yjadmin.21cnjy.com:10192")
        dr.driver.implicitly_wait(5)
        dr.is_displayed('id', 'btn-login')
        dr.click_('id', 'btn-login')
        sleep(0.5)
        dr.input_('name', 'UserName', yj1)
        dr.input_('name', 'Password', 'a123456')
        dr.click_('id', 'login-submit')

        #    {yj1}教师阅卷

        # 获取阅卷任务列表集合
        group = get_group(dr)
        # 遍历阅卷任务列表
        for i in range(len(group)):
            # 获取模式：限量、不限量
            group_pattern = get_pattern(dr, i + 1)
            initial_(dr, i + 1)
            result = online_marking(dr, group_pattern, question)
            if result != '':
                assert result_, result
                print('题组{}评阅异常，请检查'.format(i + 1))
            else:
                if i + 1 == len(group):
                    print(yj1 + '评阅完毕！')
        dr.driver.quit()

        #    登录界面
        dr = Browser()
        dr.driver.get("http://yjadmin.21cnjy.com:10192")
        dr.driver.implicitly_wait(5)
        dr.click_('id', 'btn-login')
        sleep(0.5)
        dr.input_('name', 'UserName', yj2)
        dr.input_('name', 'Password', 'a123456')
        dr.click_('id', 'login-submit')

        #    {yj2}教师阅卷
        group = get_group(dr)
        for i in range(len(group)):
            group_pattern = get_pattern(dr, i + 1)
            initial_(dr, i + 1)
            result = online_marking(dr, group_pattern)
            if result != '':
                assert result_, result
                print('题组{}评阅异常，请检查'.format(i + 1))
            else:
                if i + 1 == len(group):
                    print(yj2 + '评阅完毕！')
        dr.driver.quit()

        #    登录界面
        dr = Browser()
        dr.driver.get("http://yjadmin.21cnjy.com:10192")
        dr.driver.implicitly_wait(5)
        sleep(2)
        dr.click_('id', 'btn-login')
        sleep(0.5)
        dr.input_('name', 'UserName', yj3)
        dr.input_('name', 'Password', 'a123456')
        dr.click_('id', 'login-submit')
        sleep(2)
        #    {yj3}教师阅卷
        #    问题卷处理
        group = get_group(dr, '问题卷')
        for i in range(len(group)):
            group_pattern = get_pattern(dr, i + 1, '问题卷')
            initial_(dr, i + 1, '问题卷')
            result = online_marking(dr, group_pattern)
            if result != '':
                assert result_, result
                print('题组{}评阅异常，请检查'.format(i + 1))
            else:
                if i + 1 == len(group):
                    print(yj3 + '问题卷评阅完毕！')

        #    三评卷处理
        group = get_group(dr, '三评卷')
        for i in range(len(group)):
            group_pattern = get_pattern(dr, i + 1, '三评卷')
            initial_(dr, i + 1, '三评卷')
            result = online_marking(dr, group_pattern)
            if result != '':
                assert result_, result
                print('题组{}评阅异常，请检查'.format(i + 1))
            else:
                if i + 1 == len(group):
                    print(yj3 + '三评卷评阅完毕！')

        #    仲裁卷处理
        group = get_group(dr, '仲裁卷')
        for i in range(len(group)):
            group_pattern = get_pattern(dr, i + 1, '仲裁卷')
            initial_(dr, i + 1, '仲裁卷')
            result = online_marking(dr, group_pattern)
            if result != '':
                assert result_, result
                print('题组{}评阅异常，请检查'.format(i + 1))
            else:
                if i + 1 == len(group):
                    print(yj3 + '仲裁卷评阅完毕！')
        dr.driver.quit()
    except Exception as e:
        Browser().shot()
        raise e


if __name__ == '__main__':
    评阅试卷程序()
