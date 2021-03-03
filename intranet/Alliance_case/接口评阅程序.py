# coding=utf-8
from def_ import *
from sha_ import *
import requests
import random

# def online_marking():


def 接口评阅程序(user):
    num = 1  # 循环起始数
    headers = {}
    s = requests.session()
    rap = Rap()
    #   登陆
    while num <= 250:
        try:
            r1 = s.post(
                url='http://yjsso.21cnjy.com/Account/Login?returnurl=http:%2f%2fyjadmin.21cnjy.com:10192',
                data={
                    'UserName': user,
                    'Password': 'a123456'},
                headers=headers)
            code1 = r1.status_code
            if code1 != 200:
                pass
            else:

                #   设置Token
                r2 = s.get(
                    url='http://yjsso.21cnjy.com/Auth/GetToken?returnurl=http%3A%2F%2Fyjadmin.21cnjy.com%3A10192%2F%3FToken%3D%24Token%24',
                    headers=headers)
                code2 = r2.status_code
                if code2 != 200:
                    pass
                else:

                    #   阅卷首页
                    r3 = s.get(
                        url='http://yjadmin.21cnjy.com:10192/Home/TeacherIndex',
                        headers=headers)
                    code3 = r3.status_code
                    if code3 != 200:
                        pass
                    else:

                        #   任务列表
                        r4 = s.get(
                            url='http://yjadmin.21cnjy.com:10192/ExamOnline/List',
                            headers=headers,
                            timeout=3)
                        if r4.status_code == 200:
                            break
                        else:
                            print(r4.status_code)
        except Exception as e:
            if num == 250:
                raise e

    subject_id = rap.subjectid(r4)
    question_group_id = rap.groupid(r4)

    for i in range(len(question_group_id)):
        #   阅卷界面
        while True:
            try:
                r5 = s.get(
                    url='http://yjonline.21cnjy.com/check/CommonReview?questionGroupId={}&type=1'.format(
                        question_group_id[i]), headers=headers, timeout=3)
                if r5.status_code == 200:
                    break
            except Exception:
                pass

        data_id = rap.dataid(r5)
        max_score = rap.score(r5)
        score_list = rap.score_list(data_id, max_score)
        quality_list = rap.score_list(data_id, max_score, 'Quality')

        while True:
            try:
                #   拉取试卷
                r6 = s.get(
                    url='http://yjonline.21cnjy.com/Business/Pull?throttleNums=1&iswait=1&questionGroupId={}'.format(
                        question_group_id[i]), headers=headers)
                check_id = rap.check(r6, 'CheckId')
                teacher_id = rap.check(r6, 'TeacherId')
                #   提交阅卷
                r7 = s.post(
                    url='http://yjonline.21cnjy.com/Business/Review?questionGroupId={}'.format(question_group_id[i]),
                    json=(
                        {
                            "CheckId": "{}".format(check_id),
                            "TeacherCheckId": "{}".format(teacher_id),
                            "subjectid": "{}".format(subject_id[i]),
                            "QuestionGroupId": "{}".format(question_group_id[i]),
                            "Score": score_list,
                            "Quality": [
                                quality_list
                            ]
                        }), headers={'Content-Type': 'application/json;charset=UTF-8'})
                response = rap.response(r7)
                if response == '操作成功':
                    num += 1
            except Exception:
                '''题组评阅检查'''
                try:
                    r8 = s.get(
                        url='http://yjonline.21cnjy.com/Check/ConfirmedProcess?questionGroupId={}&viewtype=1&subjectid={}'.format(
                            question_group_id[i], subject_id[i]), headers=headers, timeout=3)
                    accomplish = rap.accomplish(r8)
                    if accomplish[0][0] >= int(accomplish[1][0]/2):
                        print(
                            user +
                            ': 题组id: {} 评阅完成'.format(
                                question_group_id[i]))
                        break
                except Exception:
                    pass


if __name__ == '__main__':
    import threading
    file = open(
        r'D:\PyCharm\projects\intranet\Alliance_case/user.txt',
        'r',
        encoding='utf-8')
    next(file)
    with file as teachers:
        teachers = teachers.read().split('\n')
    for thread in teachers:
        t = threading.Thread(target=接口评阅程序, args=(thread,))
        t.setDaemon(True)
        t.start()
    t.join()
