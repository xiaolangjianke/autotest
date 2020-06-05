"""
------------------------------------
@Time : 2019/12/20 15:50
@Auth : gaoxch  
@File : login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from case.conftest import do_conf
from time import sleep
from log.Log import Log
from page.page_object.LoginPage import LoginPage
from page.page_object.UserPage import UserPage

url = do_conf.get_locators_or_account("system", "url")
userName = do_conf.get_locators_or_account('system', 'username')
passWord = do_conf.get_locators_or_account('system', 'password')

def login(driver):
    log = Log()
    loger = log.get_log()
    loger.info("登录系统")
    login = LoginPage(driver)
    driver.get(url)
    driver.maximize_window()
    login.login_system(userName, passWord)
    sleep(1)
    user_page = UserPage(driver)
    user_page.go_to_system()
    user_page.switch_tab(2)
    title = user_page.get_title()
    assert "一企一档" in title, "进入一企一档失败，所以case失败"