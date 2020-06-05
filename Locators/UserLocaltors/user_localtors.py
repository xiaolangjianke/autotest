"""
------------------------------------
@Time : 2020/1/3 9:36
@Auth : gaoxch  
@File : user_localtors.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from utils.parseConFile import ParseConFile

do_conf = ParseConFile()
userpage = do_conf.get_locators_or_account("usermanage", "userpage")
add_button = do_conf.get_locators_or_account("usermanage", "add_button")
username = do_conf.get_locators_or_account("usermanage", "username")
password = do_conf.get_locators_or_account("usermanage", "password")
repassword = do_conf.get_locators_or_account("usermanage", "repassword")
name = do_conf.get_locators_or_account("usermanage", "name")
phone = do_conf.get_locators_or_account("usermanage", "phone")
save_button = do_conf.get_locators_or_account("usermanage", "save_button")
tooltip = do_conf.get_locators_or_account("usermanage", "tooltip")
choose_role = do_conf.get_locators_or_account("usermanage", "choose_role")
role = do_conf.get_locators_or_account("usermanage", "role")
company = do_conf.get_locators_or_account("usermanage", "company")
choose_company = do_conf.get_locators_or_account("usermanage", "choose_company")
alert_ele = do_conf.get_locators_or_account("usermanage", "alert")
ouoe = do_conf.get_locators_or_account("systems", "ouoe")