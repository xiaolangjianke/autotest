"""
------------------------------------
@Time : 2019/12/20 13:33
@Auth : gaoxch  
@File : test_useadd.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import time
import pytest

from data.TestData import login_data
from log.Log import Log

import warnings

from page.page_object.UserPage import UserPage

warnings.filterwarnings('ignore')
log = Log()
loger = log.get_log()


@pytest.mark.userTest
class TestUserAdd(object):

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, driver):
        global user_page
        user_page = UserPage(driver)
        loger.info("\n======开始执行用户管理模块case======")

    @pytest.fixture(scope="function")
    def each_case(self, everycase):
        pass

    @pytest.mark.parametrize('username,password,message,expect', login_data)
    def test_user(self, username, password, message, expect):
        time.sleep(2)
        assert expect in "一企一档", "执行失败"


if __name__ == '__main__':
    pytest.main(["-v", "test_useradd.py"])
