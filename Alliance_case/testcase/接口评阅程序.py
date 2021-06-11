# coding=utf-8
import time

from utils.sha_ import *
import requests
import threading
import os


def api_yuejuan(user):
    print('开始评阅咯！！！')
    num = 1  # 循环起始数
    headers = {}
    s = requests.session()
    rap = Rap()
    #   登陆
    while num <= 250:
        try:
            print('user：{}'.format(user))
            r1 = s.post(
                url='http://yjsso.21cnjy.com/Account/Login?returnurl=http:%2f%2fyjadmin.21cnjy.com',
                data={
                    'UserName': user,
                    'Password': 'a123456'
                },
                headers=headers
            )
            code1 = r1.status_code
            # print('r2.status_code：{}'.format(r1.status_code))
            if code1 != 200:
                pass
            else:
                #   设置Token
                r2 = s.get(
                    url='http://yjsso.21cnjy.com/Auth/GetToken',
                    params={
                        'returnurl': 'http%3A%2F%2Fyjadmin.21cnjy.com%2F%3FToken%3D%24Token%24'},
                    headers=headers,
                )
                code2 = r2.status_code
                # print('r2.status_code：{}'.format(r2.status_code))
                if code2 != 200:
                    pass
                else:

                    #   阅卷首页
                    r3 = s.get(
                        url='http://yjadmin.21cnjy.com/Home/TeacherIndex',
                        headers=headers)
                    code3 = r3.status_code
                    if code3 != 200:
                        pass
                    else:

                        #   任务列表
                        r4 = s.get(
                            url='http://yjadmin.21cnjy.com/ExamOnline/List',
                            headers=headers)
                        if r4.status_code == 200:
                            break
                        else:
                            print('r4.text：{}'.format(r4.text))
        except Exception as e:
            if num == 250:
                raise e
    question_group_id = rap.groupid(r4)
    num = 1
    for i in range(len(question_group_id)):
        #   阅卷界面
        while num <= 250:
            try:
                r5 = s.get(
                    url='http://yjonline.21cnjy.com/Check/CommonReview?questionGroupId=%s&type=1' %
                        question_group_id[i], headers=headers)
                if r5.status_code == 200:
                    break
            except Exception as e:
                if num == 250:
                    raise e
        subject_id = rap.subjectid(r5)
        data_id = rap.dataid(r5)
        max_score = rap.score(r5)
        score_list = rap.score_list(data_id, max_score)
        quality_list = rap.score_list(data_id, max_score, 'Quality')

        num = 1
        while True:
            try:
                #   拉取试卷
                r6 = s.get(
                    url='http://yjonline.21cnjy.com/Business/Pull?throttleNums=10&iswait=0&checktype=1&isFirstPull=1&subjectid={}&questionGroupId={}'.format(
                        subject_id,
                        question_group_id[i]),
                    headers=headers)
                check_id = rap.check(r6, 'CheckId')
                teacher_id = rap.check(r6, 'TeacherId')
                #   提交阅卷
                r7 = s.post(
                    url='http://yjonline.21cnjy.com/Business/Review?checkType=1&questionGroupId=%s' %
                    question_group_id[i],
                    json=(
                        {
                            "CheckId": check_id,
                            "TeacherCheckId": teacher_id,
                            "subjectid": subject_id,
                            "QuestionGroupId": question_group_id[i],
                            "Score": score_list,
                            "Quality": [quality_list]}),
                    headers={
                        'Content-Type': 'application/json;charset=UTF-8'})
                response = rap.response(r7)
                if response == '操作成功':
                    num += 1
            except Exception as e:
                '''题组评阅检查'''
                try:
                    r8 = s.get(
                        url='http://yjonline.21cnjy.com/Check/ConfirmedProcess?'
                            'questionGroupId=%s&viewtype=1&subjectid=%s' %
                            (question_group_id[i], subject_id), headers=headers)
                    accomplish = rap.accomplish(r8)
                    if accomplish[0] == accomplish[1]:
                        group_name = rap.groupname(r4, i)
                        print(
                            user +
                            ': 题组: %s 评阅完成' % group_name)
                        break
                except Exception as e:
                    if num == 250:
                        raise e

def 接口评阅程序():
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = open('%s/user.txt' % BASE_PATH, 'r', encoding='utf-8')
    next(file)
    with file as teachers:
        teachers = teachers.read().split('\n')
    for thread in teachers:  # 多线程
        t = threading.Thread(target=api_yuejuan, args=(thread,))
        t.setDaemon(True)
        t.start()
        time.sleep(2)
    t.join()


if __name__ == '__main__':
    接口评阅程序()
