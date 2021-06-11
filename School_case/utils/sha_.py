# coding=utf-8
import yagmail
import re


def user_(param):
    if param == 'username':
        return '11025688'
    elif param == 'password':
        return 'QWER1357yj'
    else:
        print('user_param == %s?' % param)


class Sha:

    def send_email(self):
        yag_server = yagmail.SMTP(
            user='774925805@qq.com',
            password='dwxardvbfunubeib',
            host='smtp.qq.com')
        email_sbject = ['774925805@qq.com']
        email_title = '阅卷测试报告'
        email_content = "UI自动化测试报告"
        # 附件
        email_attachments = [
            r'D:\PyCharm\Project\yuejuan_\School_case\Report\BeautifulReport.html']
        yag_server.send(
            email_sbject,
            email_title,
            email_content,
            email_attachments)
        yag_server.close()
