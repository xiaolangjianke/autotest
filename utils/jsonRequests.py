"""
------------------------------------
@Time : 2020/01/06 10:28
@Auth : pangmr
@File : jsonRequests.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import json
import requests
from config import config
from utils.ReadIni import Read_Ini

def jsonRequests():
    ini = Read_Ini()
    url = ini.get_value("system","jsonRequests")
    # headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}

    try:
        # 读取数据
        jsonReport = open(file=config.REPORT_DIR + '\\report.json', mode='r', encoding='utf-8')
        try:
            response = requests.post(url=url, headers=headers, data=jsonReport,timeout=10)
            print("发送json报告返回消息------->:\n",json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=2))
        except:
            print("发送json报告返回消息------->:jsonRequests地址无响应，无法发送json报告")
    except:
        print("发送json报告返回消息------->:生成json报告失败！")

if __name__ == '__main__':
    jsonRequests()