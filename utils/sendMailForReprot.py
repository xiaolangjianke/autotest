"""
------------------------------------
@Time : 2019/12/19 15:17
@Auth : gaoxch
@File : parseConFile.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""

import yagmail

from config.config import REPORT_DIR


class SendMailWithReport(object):
    '''发送邮件'''
    smtp_server = "smtp.qq.com"
    from_user = "346064730@qq.com"
    from_pass_word ="qxukpzjdnbtobjfj"
    to_user = "18896022818@163.com"
    subject = "python自动化测试"
    file_name = REPORT_DIR+"/ouoc_ui_report.html"
    @staticmethod
    def send_mail(contents):
        # 初始化服务器等信息
        yag = yagmail.SMTP(SendMailWithReport.from_user, SendMailWithReport.from_pass_word, SendMailWithReport.smtp_server)
        # 发送邮件
        yag.send(SendMailWithReport.to_user, SendMailWithReport.subject, contents, SendMailWithReport.file_name)


if __name__ == '__main__':
    SendMailWithReport.send_mail(
        "邮件正文"
    )
