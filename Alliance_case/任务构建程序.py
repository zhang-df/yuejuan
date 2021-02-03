# coding=utf-8
from def_ import *
import time
import random


def 任务构建程序():
    num = 1  # 循环起始数
    dr = Browser_()
    strf = time.strftime('%Y') + '年' + time.strftime('%m') + '月' + time.strftime('%d') + '日' + time.strftime(
        ' %H-%M-%S')
    task = u'联盟任务'
    task_name = task + strf

    # 登录进入二一阅卷
    dr.open_("http://yjadmin.21cnjy.com:10192")
    sleep(2)
    dr.is_displayed('id', 'btn-login')
    dr.click_('id', 'btn-login')
    sleep(0.5)
    dr.input_('name', 'UserName', '11025688')
    dr.input_('name', 'Password', 'a123456')
    dr.click_('id', 'login-submit')

    # 新建考试任务
    sleep(2)
    dr.driver.switch_to.frame("main-frame")
    dr.is_displayed('xpath', '//a[text()="下一页"]')
    dr.click_('xpath', "//a[text()='新建']")
    dr.click_('xpath', '//a[text()="联盟"]')
    dr.click_('xpath', '//a[text()="二一演示学校"]')
    dr.click_('xpath', '//a[text()="单元考"]')
    dr.click_('xpath', '//a[text()="一年级"]')
    dr.input_('id', 'examtask_Name', task_name)
    dr.click_('xpath', '//a[text()="校级自定义"]')
    dr.click_('xpath', '//div[text()="二维码"]')
    sleep(3)
    dr.click_('css', "[value='确定']")
    sleep(3)
    while num <= 10:
        try:
            dr.driver.find_element_by_xpath(
                '(//span[text()="准备考试"])[1]').is_displayed()
        except Exception as e:
            dr.click_('css', "[value='确定']")
            sleep(1)
            if num == 10:
                raise e
            num += 1
        else:
            break
    dr.is_displayed('xpath', '//span[text()="准备考试"]')
    dr.click_('xpath', '(//label[contains(@onclick,"location")])[1]')

    # 科目设置
    dr.click_('xpath', "//a[text()='新建']")
    dr.click_('xpath', "//a[text()='语文']")
    dr.input_('name', 'FullScore', '150')
    dr.mouse('xpath', "//button[text()='提交']")
    dr.is_displayed('xpath', '//td[text()="语文"]')
    dr.click_('xpath', "//a[text()='新建']")
    dr.click_('xpath', "//a[text()='数学']")
    dr.input_('name', 'FullScore', '120')
    dr.mouse('xpath', "//button[text()='提交']")
    dr.is_displayed('xpath', '//td[text()="数学"]')
    print('科目新建完毕')

    # 题卡制作
    # 科目一
    dr.click_('xpath', '//a[text()="2.试卷及题卡制作"]')
    dr.click_('xpath', '(//a[contains(@title,"制作题卡")])[1]')
    sleep(1)
    dr.input_('id', 'TiKaTitle', '自动化空白题卡')
    dr.click_('id', 'btn-empty-create')
    sleep(3)
    dr.click_('xpath', '//tr[contains(@data-name,"语文")]')
    dr.is_displayed('xpath', '//td[text()="0"]')

    # 切换窗口
    dr.handles_(-1)
    dr.click_('xpath', '//li[text()="A3二栏"]')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(1)
    dr.click_('xpath', '//a[text()="二维码"]')
    sleep(0.5)
    dr.click_('xpath', '(//a[text()="否"])[1]')
    dr.click_('xpath', '(//a[text()="是"])[2]')
    sleep(0.5)

    # 添加题目
    dr.click_('xpath', '//a[text()="+ 客观题"]')
    sleep(0.5)
    dr.double_click('name', 'count')
    dr.get_position('name', 'count').send_keys('5')
    dr.click_('xpath', '(//span[contains(@class,"btn-inc btn")])[6]')
    dr.click_('xpath', '(//span[contains(@class,"btn-dec btn")])[9]')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '(//div[contains(@class,"tka-choice")])[1]')
    dr.click_('css', '[title="添加题目"]')
    sleep(0.5)
    dr.click_('xpath', '(//span[text()="单选题"])[1]')
    dr.click_('xpath', '//span[text()="判断题"]')
    dr.double_click('name', 'count')
    dr.get_position('name', 'count').send_keys('5')
    dr.click_('xpath', '(//span[contains(@class,"btn-inc btn")])[6]')
    dr.click_('xpath', '(//span[contains(@class,"btn-dec btn")])[9]')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '(//div[contains(@class,"tka-choice")])[1]')
    dr.click_('css', '[title="添加题目"]')
    sleep(0.5)
    dr.click_('xpath', '(//span[text()="单选题"])[1]')
    dr.click_('xpath', '//span[text()="多选题（标准）"]')
    dr.double_click('name', 'count')
    dr.get_position('name', 'count').send_keys('10')
    dr.click_('xpath', '(//span[contains(@class,"btn-inc btn")])[6]')
    dr.click_('xpath', '(//span[contains(@class,"btn-dec btn")])[9]')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="+ 客观题"]')
    sleep(0.5)
    dr.click_('xpath', '(//span[text()="单选题"])[1]')
    dr.click_('xpath', '//span[text()="多选题（三段分）"]')
    dr.double_click('name', 'count')
    dr.get_position('name', 'count').send_keys('5')
    dr.input_('name', 'startN', '1')
    dr.click_('xpath', '(//span[contains(@class,"btn-inc btn")])[6]')
    dr.click_('xpath', '(//span[contains(@class,"btn-inc btn")])[7]')
    dr.click_('xpath', '(//span[contains(@class,"btn-dec btn")])[9]')
    dr.click_('xpath', '(//span[contains(@class,"btn-dec btn")])[10]')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="+ 填空题"]')
    sleep(0.5)
    dr.double_click('name', 'count')
    dr.get_position('name', 'count').send_keys('5')
    dr.double_click('name', 'scor')
    dr.get_position('name', 'scor').send_keys('4')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="+ 解答题"]')
    sleep(0.5)
    dr.double_click('name', 'count')
    dr.get_position('name', 'count').send_keys('5')
    dr.double_click('name', 'scor')
    dr.get_position('name', 'scor').send_keys('6')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '(//i[text()="添加小题"])[9]')
    dr.double_click('name', 'count')
    dr.driver.find_element_by_name('count').send_keys(6)
    dr.input_('name', 'scor', 1)
    dr.click_('xpath', '(//i[@class="icon icons-radio"])[2]')
    dr.double_click('name', 'ans_rows')
    dr.driver.find_element_by_name('ans_rows').send_keys(2)
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="+ 语文作文"]')
    sleep(0.5)
    dr.click_('xpath', '(//span[text()="800 字"])[1]')
    dr.click_('xpath', '//span[text()="100 字"]')
    dr.input_('name', 'score', '25')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="+ 英语作文"]')
    sleep(0.5)
    dr.click_('xpath', '(//span[text()="10 行"])[1]')
    dr.click_('xpath', '//span[text()="3 行"]')
    dr.input_('name', 'score', '25')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="+ 综合题"]')
    dr.input_('name', 'scor[]', 4)
    dr.input_('name', 'count', 2)
    dr.click_('xpath', '(//a[@class="btn-mtype "])[1]')
    dr.input_('name', 'count', 2)
    dr.click_('xpath', '(//a[@class="btn-mtype"])[2]')
    dr.input_('name', 'count', 2)
    dr.click_('xpath', '(//a[@class="btn-mtype"])[3]')
    dr.input_('name', 'count', 2)
    dr.click_('xpath', '(//a[@class="btn-mtype"])[4]')
    dr.input_('name', 'count', 2)
    dr.click_('xpath', '//span[text()="设为附加题"]')
    dr.click_('xpath', '//span[text()="确定"]')
    sleep(0.5)
    dr.click_('id', 'tika-formdata-submit')
    dr.is_displayed('xpath', '//div[text()="提交成功"]')
    sleep(1)
    dr.driver.close()
    dr.handles_(0)
    dr.driver.switch_to.frame("main-frame")

    # 客观题设置
    single = ('A', 'B', 'C', 'D')
    judgment = ('T', 'F')
    multiselect_3 = ('A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC')
    multiselect_4 = (
        'A',
        'B',
        'C',
        'D',
        'AB',
        'AC',
        'AD',
        'BC',
        'BD',
        'CD',
        'ABC',
        'ABD',
        'BCD',
        'ABD',
        'ABCD')

    dr.click_('xpath', '//a[text()="客观题设置"]')
    dr.is_displayed('id', 'isPlusType')
    dr.click_('id', 'isPlusType')
    dr.click_('xpath', '//a[text()="导入答案"]')
    sleep(1)
    element_1 = dr.driver.find_element_by_id("sCount_Need").text
    number1 = int(element_1)
    for i in range(number1):
        key_1 = random.choice(single)
        dr.driver.find_element_by_id('single').send_keys(key_1)
    element_2 = dr.driver.find_element_by_id("jCount_Need").text
    number2 = int(element_2)
    for i in range(number2):
        key_2 = random.choice(judgment)
        dr.driver.find_element_by_id('judge').send_keys(key_2)
    element_3 = dr.driver.find_element_by_id("mCount_Need").text
    number3 = int(element_3)
    for i in range(number3):
        key_3 = random.choice(multiselect_4)
        dr.driver.find_element_by_id('multiple').send_keys(key_3)
        dr.driver.find_element_by_id('multiple').send_keys(',')
    dr.driver.find_element_by_id('multiple').send_keys(Keys.BACKSPACE)
    dr.click_('name', 'InsertAnswer')
    dr.is_displayed('xpath', '//span[text()="答案导入成功"]')
    sleep(3)

    # 知识点设置
    dr.click_('xpath', '//a[text()="知识点设置"]')
    dr.is_displayed('xpath', '//th[text()="知识点"]')
    dr.js_('xpath', '//td[text()="英语作文"]')
    sleep(1)
    dr.click_('xpath', '(//tr[@data-typecode="23"]/td/div/div)[2]/button')
    dr.is_displayed('xpath', '//div[text()="请选择知识点"]')
    sleep(2)
    dr.click_('xpath', '//em[text()="一年级上册"]')
    dr.is_displayed('xpath', '//em[text()="识字（一）"]')
    dr.click_('xpath', '//em[text()="识字（一）"]')
    dr.is_displayed('xpath', '//em[text()="1 天地人"]')
    dr.click_('xpath', '//em[text()="1 天地人"]')
    dr.is_displayed('xpath', '//input[@ztxt="天地人"]')
    dr.click_('xpath', '//input[@ztxt="天地人"]')
    dr.click_('xpath', '//em[text()="2 金木水火土"]')
    dr.is_displayed('xpath', '//input[@ztxt="金木水火土"]')
    dr.click_('xpath', '//input[@ztxt="金木水火土"]')
    dr.click_('xpath', '//em[text()="3 口耳目"]')
    dr.is_displayed('xpath', '//input[@ztxt="口耳目"]')
    dr.click_('xpath', '//input[@ztxt="口耳目"]')
    dr.click_('xpath', '//em[text()="4 日月水火"]')
    dr.is_displayed('xpath', '//input[@ztxt="日月水火"]')
    dr.click_('xpath', '//input[@ztxt="日月水火"]')
    dr.click_('xpath', '//em[text()="5 对韵歌"]')
    dr.is_displayed('xpath', '//input[@ztxt="对韵歌"]')
    dr.click_('xpath', '//input[@ztxt="对韵歌"]')
    dr.click_('xpath', '//button[text()="确定"]')
    sleep(1)
    dr.click_('xpath', '(//tr[@data-typecode="24"]/td/div/div)[2]/button')
    dr.is_displayed('xpath', '//div[text()="请选择知识点"]')
    sleep(1)
    dr.js_('xpath', '//em[text()="汉语拼音"]')
    dr.click_('xpath', '//em[text()="汉语拼音"]')
    dr.click_('xpath', '//em[text()="1 a o e"]')
    dr.is_displayed('xpath', '//input[@ztxt="aoe"]')
    dr.click_('xpath', '//input[@ztxt="aoe"]')
    dr.click_('xpath', '//em[text()="2 i u ü y w"]')
    dr.is_displayed('xpath', '//input[@ztxt="iuü"]')
    dr.click_('xpath', '//input[@ztxt="iuü"]')
    dr.click_('xpath', '//em[text()="3 b p m f"]')
    dr.is_displayed('xpath', '//input[@ztxt="bpmf"]')
    dr.click_('xpath', '//input[@ztxt="bpmf"]')
    dr.click_('xpath', '//em[text()="4 d t n l"]')
    dr.is_displayed('xpath', '//input[@ztxt="dtnl"]')
    dr.click_('xpath', '//input[@ztxt="dtnl"]')
    dr.click_('xpath', '//em[text()="5 g k h"]')
    dr.is_displayed('xpath', '//input[@ztxt="gkh"]')
    dr.click_('xpath', '//input[@ztxt="gkh"]')
    dr.click_('xpath', '//button[text()="确定"]')
    sleep(1)

    # 技能设置
    dr.js_('xpath', '//a[text()="技能设置"]')
    dr.click_('xpath', '//a[text()="技能设置"]')
    dr.is_displayed('xpath', '//input[@value="启用"]')
    dr.click_('xpath', '(//input)[1]')
    dr.click_('xpath', '(//input)[2]')
    dr.click_('xpath', '(//input)[3]')
    dr.click_('xpath', '//input[@value="启用"]')
    dr.is_displayed('xpath', '//th[text()="学习水平"]')
    dr.is_displayed('xpath', '//th[text()="内容分布"]')
    dr.is_displayed('xpath', '//th[text()="学业质量标准"]')

    # 科目二
    dr.click_('xpath', '//a[text()="试卷制作"]')
    dr.is_displayed('xpath', '(//a[contains(@title,"制作题卡")])[1]')
    dr.click_('xpath', '(//a[contains(@title,"制作题卡")])[1]')
    sleep(1)
    dr.click_(
        'xpath',
        '//label[@style="margin-right:10px;position: relative;"]')
    sleep(0.5)
    dr.input_('id', 'search-key', '自动化组卷题卡')
    sleep(0.5)
    dr.click_('id', 'btn-search')
    sleep(2)
    dr.is_displayed(
        'xpath',
        '//input[@value="1997139"]')
    dr.click_('xpath', '//input[@value="1997139"]')
    dr.click_('id', 'btn-zujuan-create')
    dr.is_displayed('xpath', '(//a[contains(@title,"编辑题卡")])[2]')
    sleep(1)
    dr.click_('xpath', '//td[text()="数学"]')

    # 客观题设置
    dr.click_('xpath', '//a[text()="客观题设置"]')
    dr.is_displayed('xpath', '//a[text()="导入答案"]')
    dr.click_('xpath', '//a[text()="导入答案"]')
    sleep(1)
    element_1 = dr.driver.find_element_by_id("sCount_Need").text
    number1 = int(element_1)
    dr.driver.find_element_by_id('single').clear()
    for i in range(number1):
        key_1 = random.choice(single)
        dr.driver.find_element_by_id('single').send_keys(key_1)
    element_2 = dr.driver.find_element_by_id("jCount_Need").text
    number2 = int(element_2)
    dr.driver.find_element_by_id('judge').clear()
    for i in range(number2):
        key_2 = random.choice(judgment)
        dr.driver.find_element_by_id('judge').send_keys(key_2)
    element_3 = dr.driver.find_element_by_id("mCount_Need").text
    number3 = int(element_3)
    dr.driver.find_element_by_id('multiple').clear()
    for i in range(number3 - 5):
        key_3 = random.choice(multiselect_4)
        dr.driver.find_element_by_id('multiple').send_keys(key_3)
        dr.driver.find_element_by_id('multiple').send_keys(',')
    for i in range(number3 - 10):
        key_3 = random.choice(multiselect_3)
        dr.driver.find_element_by_id('multiple').send_keys(key_3)
        dr.driver.find_element_by_id('multiple').send_keys(',')
    dr.driver.find_element_by_id('multiple').send_keys(Keys.BACKSPACE)
    dr.click_('name', 'InsertAnswer')
    dr.is_displayed('xpath', '//span[text()="答案导入成功"]')
    sleep(3)
    print('题卡制作完毕')

    # 技能设置
    dr.js_('xpath', '//a[text()="技能设置"]')
    dr.click_('xpath', '//a[text()="技能设置"]')
    dr.is_displayed('xpath', '//input[@value="启用"]')
    dr.click_('xpath', '(//input)[4]')
    dr.click_('xpath', '(//input)[5]')
    dr.click_('xpath', '(//input)[6]')
    dr.click_('xpath', '//input[@value="启用"]')
    dr.is_displayed('xpath', '//th[text()="学习水平"]')
    dr.is_displayed('xpath', '//th[text()="内容分布"]')
    dr.is_displayed('xpath', '//th[text()="核心素养"]')
    sleep(1)

    # 参考科目
    dr.click_('xpath', '//a[text()="3.参考科目"]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[2]')
    dr.mouse('xpath', "//a[text()='批量设置参考科目']")
    dr.driver.switch_to.frame("layui-layer-iframe1")
    dr.click_('id', 'selectAll')
    dr.driver.switch_to.parent_frame()
    dr.click_('xpath', "//a[text()='确定']")
    sleep(2)
    dr.is_displayed('xpath', '//td[text()="语文,数学"]')
    dr.Select_('text', 'id', 'examschool', 'T2二一演示')
    dr.is_displayed('xpath', '(//td[text()="无参考科目"])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[2]')
    dr.mouse('xpath', "//a[text()='批量设置参考科目']")
    dr.driver.switch_to.frame("layui-layer-iframe1")
    dr.click_('id', 'selectAll')
    dr.driver.switch_to.parent_frame()
    dr.click_('xpath', "//a[text()='确定']")
    sleep(2)
    dr.is_displayed('xpath', '//td[text()="语文,数学"]')
    dr.Select_('text', 'id', 'examschool', 'T3二一演示')
    dr.is_displayed('xpath', '(//td[text()="无参考科目"])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[2]')
    dr.mouse('xpath', "//a[text()='批量设置参考科目']")
    dr.driver.switch_to.frame("layui-layer-iframe1")
    dr.click_('id', 'selectAll')
    dr.driver.switch_to.parent_frame()
    dr.click_('xpath', "//a[text()='确定']")
    sleep(2)
    dr.is_displayed('xpath', '//td[text()="语文,数学"]')
    dr.Select_('text', 'id', 'examschool', 'T4二一演示')
    dr.is_displayed('xpath', '(//td[text()="无参考科目"])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[2]')
    dr.mouse('xpath', "//a[text()='批量设置参考科目']")
    dr.driver.switch_to.frame("layui-layer-iframe1")
    dr.click_('id', 'selectAll')
    dr.driver.switch_to.parent_frame()
    dr.click_('xpath', "//a[text()='确定']")
    sleep(2)
    dr.is_displayed('xpath', '//td[text()="语文,数学"]')
    dr.Select_('text', 'id', 'examschool', 'T5二一演示')
    dr.is_displayed('xpath', '(//td[text()="无参考科目"])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[1]')
    dr.click_('xpath', '(//input[contains(@name,"op")])[2]')
    dr.mouse('xpath', "//a[text()='批量设置参考科目']")
    dr.driver.switch_to.frame("layui-layer-iframe1")
    dr.click_('id', 'selectAll')
    dr.driver.switch_to.parent_frame()
    dr.click_('xpath', "//a[text()='确定']")
    sleep(2)
    dr.is_displayed('xpath', '//td[text()="语文,数学"]')
    print('班级参考完毕')

    # 题组设置
    dr.click_('xpath', '//a[text()="5.任务分配"]')

    # 科目一
    # 合并评分点
    dr.driver.switch_to.frame('main-frame')
    dr.is_displayed("xpath", '(//span[text()="未设置"])[1]')
    dr.click_('id', 'btn-viewti')
    dr.driver.switch_to.frame("layui-layer-iframe2")
    dr.is_displayed('xpath', '(//tr[contains(@data-optioncount,"0")])[1]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[1]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[2]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[3]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[4]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[5]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[1]')
    sleep(0.5)
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[2]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[3]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[4]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[12]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[2]')
    sleep(0.5)
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[4]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[5]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[8]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[9]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[3]')
    sleep(0.5)
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[5]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[6]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[4]')
    sleep(0.5)
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[8]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[9]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[10]')
    dr.click_('xpath', '(//tr[contains(@data-optioncount,"0")])[11]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[5]')
    sleep(0.5)
    dr.driver.switch_to.parent_frame()
    dr.click_('xpath', '//a[text()="确定"]')
    sleep(1)
    dr.is_displayed('xpath', '//td[text()="7.24~7.27 (附)"]')

    # 添加题组
    dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.input_('id', 'topic-name', u'不限量-单评')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='单评']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    dr.is_displayed("xpath", "//span[text()='不限量-单评']")
    sleep(1)
    dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.input_('id', 'topic-name', u'不限量-双评')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='双评']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    dr.is_displayed("xpath", "//span[text()='不限量-双评']")
    sleep(1)
    dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.input_('id', 'topic-name', u'不限量-二加一')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='2+1']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    dr.is_displayed("xpath", "//span[text()='不限量-二加一']")
    sleep(1)
    dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.input_('id', 'topic-name', u'不限量-二加一加一')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='2+1+1']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    dr.is_displayed("xpath", "//span[text()='不限量-二加一加一']")
    dr.click_('css', '[class="group-title"]')
    sleep(1)
    # 所属题组
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[1]",
        '不限量-单评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[2]",
        '不限量-单评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[3]",
        '不限量-单评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[4]",
        '不限量-双评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[5]",
        '不限量-双评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[6]",
        '不限量-二加一')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[7]",
        '不限量-二加一加一')
    dr.input_(
        'xpath',
        "(//input[contains(@class,'control-critical form-control width-auto mini')])[6]",
        '25')
    dr.input_(
        'xpath',
        "(//input[contains(@class,'control-critical form-control width-auto mini')])[7]",
        '16')
    dr.click_('xpath', "//button[text()='保存']")
    sleep(1)
    dr.is_displayed('xpath', '//span[text()="2+1+1"]')
    dr.click_('id', 'btn-confirmed')
    dr.is_displayed('xpath', '//a[text()="题组结构确认成功"]')
    sleep(1)

    # 科目二
    # 添加题组
    dr.click_('xpath', '//a[text()="数学"]')
    dr.is_displayed("xpath", '(//span[text()="未设置"])[1]')
    dr.click_('id', 'btn-viewti')
    dr.driver.switch_to.frame("layui-layer-iframe18")
    dr.is_displayed('xpath', '(//tr[@data-optionjson="[null]"])[1]')
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[1]')
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[2]')
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[3]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[1]')
    sleep(1)
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[1]')
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[2]')
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[3]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[2]')
    sleep(1)
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[1]')
    dr.click_('xpath', '(//tr[@data-optionjson="[null]"])[2]')
    sleep(0.5)
    dr.click_('xpath', '//a[text()="合并评分点"]')
    dr.is_displayed('xpath', '(//td[text()="是"])[3]')
    sleep(1)
    dr.driver.switch_to.parent_frame()
    dr.click_('xpath', '//a[text()="确定"]')
    dr.is_displayed('xpath', '//td[text()="4.26~4.28 "]')
    sleep(1)
    dr.click_('xpath', "//a[text()='添加题组']")
    try:
        dr.driver.find_element_by_xpath('//div[text()="添加题组"]').is_displayed()
    except Exception:
        dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.click_('xpath', '//a[text()="限量"]')
    sleep(0.5)
    dr.input_('id', 'topic-name', u'限量-单评')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='单评']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    sleep(1)
    dr.is_displayed("xpath", "//span[text()='限量-单评']")
    dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.input_('id', 'topic-name', u'限量-双评')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='双评']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    dr.is_displayed("xpath", "//span[text()='限量-双评']")
    sleep(1)
    dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.input_('id', 'topic-name', u'限量-二加一')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='2+1']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    dr.is_displayed("xpath", "//span[text()='限量-二加一']")
    sleep(1)
    dr.click_('xpath', "//a[text()='添加题组']")
    sleep(0.5)
    dr.input_('id', 'topic-name', u'限量-二加一加一')
    sleep(0.5)
    dr.click_('xpath', "//a[text()='2+1+1']")
    sleep(0.5)
    dr.click_('xpath', '//button[text()="提交"]')
    dr.is_displayed("xpath", "//span[text()='限量-二加一加一']")
    dr.click_('css', '[class="group-title"]')
    sleep(1)
    # 所属题组
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[1]",
        '限量-单评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[2]",
        '限量-单评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[3]",
        '限量-单评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[4]",
        '限量-双评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[5]",
        '限量-双评')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[6]",
        '限量-二加一')
    dr.Select_(
        'text',
        'xpath',
        "(//select[contains(@name,'questionGroupId')])[7]",
        '限量-二加一加一')
    dr.input_(
        'xpath',
        "(//input[contains(@class,'control-critical form-control width-auto mini')])[6]",
        '15')
    dr.input_(
        'xpath',
        "(//input[contains(@class,'control-critical form-control width-auto mini')])[7]",
        '15')
    dr.click_('xpath', "//button[text()='保存']")
    sleep(2)
    dr.is_displayed('xpath', '//span[text()="2+1+1"]')
    dr.click_('id', 'btn-confirmed')
    dr.is_displayed('xpath', '//a[text()="题组结构确认成功"]')
    sleep(1)
    print('题组设置完毕')
    dr.driver.quit()
