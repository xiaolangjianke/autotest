"""
------------------------------------
@Time : 2019/12/26 14:55
@Auth : gaoxch
@File : run.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from config.config import *
from utils.jsonRequests import jsonRequests

case_path = CASE_DIR
html_report_path = REPORT_DIR


# def runcase(name="chrome", cases_path=""):
#     '''
#
#     :param name:
#     :param cases_path:
#     :return:
#     '''
#     os.system(
#         "pytest -v -s --browser=%s %s --host=https://nav.asoco.com.cn/login --html=%s/oeoa_ui_report.html --self-contained-html  "
#         % (name, case_path, html_report_path))

def runcase(name="chrome", cases_path=""):
    if (os.path.exists(REPORT_DIR + '\\report.json')):
        os.remove(REPORT_DIR + '\\report.json')
    # 执行路径下的所有case
    # os.system(
    #     "pytest -v -s --browser=%s %s  --host=https://nav.asoco.com.cn/login --json=%s/report.json --jsonapi "
    #     % (name, case_path, html_report_path))
    # 执行某个模块下的case
    os.system(
        "pytest -m userTest --browser=%s %s  --host=https://nav.asoco.com.cn/login --json=%s/report.json --jsonapi "
        % (name, case_path, html_report_path))
    jsonRequests()


if __name__ == '__main__':
    case_path = case_path
    runcase(cases_path=case_path)
