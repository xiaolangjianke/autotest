"""
------------------------------------
@Time : 2019/12/19 17:10
@Auth : gaoxch  
@File : LoginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from time import sleep

from Locators.LoginLocaltors import login_localtors as ll
from page.BasePage import BasePage


class LoginPage(BasePage):

    def login_system(self, username, password):
        # 登录操作
        self.send_keys(*ll.username, username)
        self.send_keys(*ll.password, password)
        self.click(*ll.button)
        # 获取登录失败系统提示
        text = self.get_element_text(*ll.tooltip)
        # 获取title
        title = self.get_title()
        return
        # try:
        #     # 退出登录
        #     self.click_loginout()
        # except:
        #     self.loger.info("登录失败")
