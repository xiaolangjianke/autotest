"""
------------------------------------
@Time : 2019/12/19 14:50
@Auth : gaoxch  
@File : TestData.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from utils.ExcelUtils import ExcelUtils

login = ExcelUtils(index="Sheet1").get_data()
login_data = ExcelUtils(index="login_data").get_data()
