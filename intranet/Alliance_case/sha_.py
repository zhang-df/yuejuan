# coding=utf-8
import yagmail
import random
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
            r'D:\PyCharm\projects\intranet\Alliance_case\Report\YJ_report.html']
        yag_server.send(
            email_sbject,
            email_title,
            email_content,
            email_attachments)
        yag_server.close()


class Rap:

    def access_token(self, request, value):
        """提取access_token"""
        string = str(request.text)
        pattern = r'"access_token":"(.+?)",'
        access_token = re.findall(pattern, string)
        return access_token[value]

    def subjectid(self, request):
        """提取subjectid"""
        subject_list = []
        string = str(request.text)
        pattern_1 = r'学科：(.*?)</div>'
        subject = re.findall(pattern_1, string)
        for i in range(len(subject)):
            pattern_2 = r'<option value="(.*?)" >%s</option>' % subject[i]
            subject_id = re.findall(pattern_2, string)
            subject_list.append(int(subject_id[0]))
        return subject_list

    def groupid(self, request):
        """提取questionGroupId"""
        string = str(request.text)
        pattern = r'questionGroupId=(.+?)&'
        group_list = re.findall(pattern, string)
        group_list.append(group_list[0])
        return group_list[1:]

    def total_quantity(self, request, value):
        """提取题组number"""
        string = str(request.text)
        pattern = r'总量 :\d+/(.+?) '
        total_quantity = re.findall(pattern, string)
        total_quantity = int(total_quantity[value])
        return total_quantity

    def dataid(self, request):
        """提取data-id"""
        string = str(request.text)
        pattern = r'data-id="(.+?)" data-max='
        topic_list = re.findall(pattern, string)
        return topic_list

    def score(self, request):
        """提取题目score"""
        string = str(request.content)
        pattern = r'data-max="(.+?)"'
        score_list = re.findall(pattern, string)
        return score_list

    def check(self, request, value):
        """提取CheckId"""
        string = str(request.content)
        if value == 'CheckId':
            pattern = r'"CheckId":"(.+?)"'
        elif value == 'TeacherId':
            pattern = r'"TeacherCheckId":"(.+?)"'
        ele = re.findall(pattern, string)
        return ele[0]

    def score_list(self, data_id, max_score, quality=None):
        """
        :param data_id: 题目id
        :param max_score: 题目满分
        :param quality: quality
        :return: score_list
        """
        score_list = []
        for i in range(len(data_id)):
            if quality:
                score_list.append({"Key": data_id[i], "Value": random.randint(0, 2)})
            else:
                score_list.append({"Key": data_id[i], "Value": random.randint(0, int(max_score[i]))})
        return score_list

    def response(self, request):
        """提取响应内容"""
        string = str(request.text)
        pattern = r'"Message":"(.+?)",'
        response = re.findall(pattern, string)
        response = str(response[0])
        return response

    def accomplish(self, request):
        """提取题组完成量"""
        string = str(request.text)
        pattern1 = '"IReadCount":(.*?),"'
        pattern2 = '"QGAllCount":(.*?),"'
        response1 = list(map(int, re.findall(pattern1, string)))
        response2 = list(map(int, re.findall(pattern2, string)))
        return response1, response2
