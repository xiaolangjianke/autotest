"""
------------------------------------
@Time : 2019/12/20 13:02
@Auth : gaoxch  
@File : UserPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from time import sleep

from Locators.UserLocaltors import user_localtors as ul
from page.BasePage import BasePage
from utils.parseConFile import ParseConFile


class UserPage(BasePage):
    # do_conf = ParseConFile()
    # userpage = do_conf.get_locators_or_account("usermanage", "userpage")
    # add_button = do_conf.get_locators_or_account("usermanage", "add_button")
    # username = do_conf.get_locators_or_account("usermanage", "username")
    # password = do_conf.get_locators_or_account("usermanage", "password")
    # repassword = do_conf.get_locators_or_account("usermanage", "repassword")
    # name = do_conf.get_locators_or_account("usermanage", "name")
    # phone = do_conf.get_locators_or_account("usermanage", "phone")
    # save_button = do_conf.get_locators_or_account("usermanage", "save_button")
    # tooltip = do_conf.get_locators_or_account("usermanage", "tooltip")
    # choose_role = do_conf.get_locators_or_account("usermanage", "choose_role")
    # role = do_conf.get_locators_or_account("usermanage", "role")
    # company = do_conf.get_locators_or_account("usermanage", "company")
    # choose_company = do_conf.get_locators_or_account("usermanage", "choose_company")
    # alert_ele = do_conf.get_locators_or_account("usermanage", "alert")
    # ouoe = do_conf.get_locators_or_account("systems", "ouoe")

    def go_to_system(self):
        self.click_and_click(ul.ouoe)
        sleep(1)

    def addUser(self, user, password, repassword, name, phone):
        self.click_addUser()
        sleep(1)
        self.send_username(user)
        self.send_password(password)
        self.send_repassword(repassword)
        self.send_name(name)
        self.send_phone(phone)
        self.chooseCompany()
        self.chooseRole()
        self.click_save_button()
        sleep(0.5)

    def chooseRole(self):
        self.click_role()
        sleep(0.5)
        self.click(*ul.choose_role)

    def click_role(self):
        self.click(*ul.role)

    def click_userPage(self):
        self.click(*ul.userpage)

    def click_addUser(self):
        self.click(*ul.add_button)

    def send_username(self, user):
        self.send_keys(*ul.username, user)

    def send_password(self, password):
        self.send_keys(*password, password)

    def send_repassword(self, repassword):
        self.send_keys(*ul.repassword, repassword)

    def send_name(self, name):
        self.send_keys(*ul.name, name)

    def send_phone(self, phone):
        self.send_keys(*ul.phone, phone)

    def click_save_button(self):
        sleep(1)
        self.click(*ul.save_button)

    def get_tooltip(self):
        self.get_element_text(*ul.tooltip)

    def chooseCompany(self):
        self.click_company()
        sleep(0.5)
        self.click(*ul.choose_company)

    def click_company(self):
        self.click(*ul.company)

    def click_alert(self):
        self.click(*ul.alert_ele)

    def get_text(self):
        self.get_element_text(*ul.tooltip)

if __name__ == '__main__':
    driver = 1
    a = UserPage(driver=driver)
    a.click_addUser()


