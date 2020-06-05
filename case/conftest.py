# import pytest
# from selenium import webdriver
# from common.Login import Login
# from log.Log import Log
# from utils.ReadIni import Read_Ini

# log = Log().get_log()
# ini = Read_Ini()
#
# # 创建driver，并返回全局--自动运行
# @pytest.fixture(scope="session", autouse=True)
# def driver():
#     global driver
#
#     options = webdriver.ChromeOptions()
#     options.set_headless(True)
#     options.add_argument('--window-size=1920x1080')
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#
#     login = Login(driver)
#     login.login()
#
#     return driver
#
#
# # 浏览器刷新--手动调用
# @pytest.fixture(scope="function")
# def Refresh(driver):
#     log.info("===刷新浏览器===")
#     driver.refresh()
#     yield
#     log.info("该条用例测试结束")
#
#
# # 整个项目自动化代码运行完直接关闭--自动运行
# @pytest.fixture(scope="session" , autouse=True)
# def Quit(driver):
#     pass
#     yield
#     log.info("===关闭浏览器===")
#     driver.quit()
#
#
# # pytest-html报告自定义--自动运行
# def pytest_configure(config):
#     config._metadata['project'] = ini.get_value("system", "system")
#     config._metadata['url'] = ini.get_value("system", "url")
#     config._metadata['id' ] = ini.get_value("system", "id")
#     config._metadata['pwd'] = ini.get_value("system", "pwd")
#
#
# # pytest-json报告自定义--自动运行
# @pytest.fixture(scope='session', autouse=True)
# def extra_json_environment(request):
#     request.config._json_environment.append(('project', ini.get_value("system", "system")))
#     request.config._json_environment.append(('url', ini.get_value("system", "url")))
#     request.config._json_environment.append(('id', ini.get_value("system", "id")))
#     request.config._json_environment.append(('pwd', ini.get_value("system", "pwd")))
import pytest

from page.page_object.LoginPage import LoginPage
from page.page_object.UserPage import UserPage
from utils.parseConFile import ParseConFile
from log.Log import Log
do_conf = ParseConFile()
# 通过配置文件获取正确的用户名和密码
userName = do_conf.get_locators_or_account('system', 'username')
passWord = do_conf.get_locators_or_account('system', 'password')
log = Log()
loger = log.get_log()
driver = 1

# @pytest.fixture(scope='class')
# def ini_pages(driver):
#     login_page = LoginPage(driver)
#     user_page = UserPage(driver)
#     yield driver, login_page, user_page
#
#
# @pytest.fixture(scope='function')
# def open_url(ini_pages):
#     ''' 获取当前页的page '''
#     driver = ini_pages[0]
#     login_page = ini_pages[1]
#     user_page = ini_pages[2]
#     yield login_page,user_page
#     driver.quit()
#
#
# @pytest.fixture(scope='class')
# def login(ini_pages):
#     driver, login_page, user_page = ini_pages
#     # login_page.open_url()
#     login_page.login_system(userName, passWord)
#     yield driver, login_page, user_page
#     driver.delete_all_cookies()
#
#
# @pytest.fixture(scope='function')
# def logout(ini_pages):
#     driver, login_page = ini_pages
#     driver.delete_all_cookies()
#
#
# @pytest.fixture(scope='function')
# def refresh_page(ini_pages):
#
#     driver = ini_pages[0]
#     login_page = ini_pages[1]
#     user_page = ini_pages[2]
#     yield driver,login_page,user_page
#     driver.refresh()
#     print("刷新了")

@pytest.fixture(scope="function",autouse=True)
def everycase(driver):
    """
    应急物资与环保管理前置条件与后置条件
    前置条件：刷新浏览器
    后置条件：说明case执行完毕，并输出到日志文件
    """
    loger.info("\n刷新浏览器")

    yield
    loger.info("\n本条case执行完毕")
    driver.refresh()