# coding=utf-8
import yagmail
import re


class Sha:

    def send_email(self):
        yag_server = yagmail.SMTP(
            user='851379672@qq.com',
            password='zyupulzizutibbca',
            host='smtp.qq.com')
        email_sbject = ['851379672@qq.com']
        email_title = '阅卷测试报告'
        email_content = "UI自动化测试报告"
        # 附件
        email_attachments = [
            r'D:\PyCharm\projects\intranet\School_case\Report\YJ_report.html']
        yag_server.send(
            email_sbject,
            email_title,
            email_content,
            email_attachments)
        yag_server.close()
