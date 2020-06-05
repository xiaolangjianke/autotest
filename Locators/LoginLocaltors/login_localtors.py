"""
------------------------------------
@Time : 2020/1/2 15:28
@Auth : gaoxch  
@File : login_localtors.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from utils.parseConFile import ParseConFile

do_conf = ParseConFile()
# 用户名元素
username = do_conf.get_locators_or_account("login", "username")
# 用户密码元素
password = do_conf.get_locators_or_account("login", "password")
# 登录按钮元素
button = do_conf.get_locators_or_account("login", "button")
# 登录失败提示元素
tooltip = do_conf.get_locators_or_account("login", "tooltip")
# 登录成功后退出登录元素
loginout = do_conf.get_locators_or_account("login","loginout")