import pytest
from common.login import login
from selenium import webdriver
from py.xml import html
from log.Log import Log
from utils.ReadIni import Read_Ini

_driver = None
log = Log()
logger = log.get_log()
ini = Read_Ini()
def pytest_addoption(parser):
    '''添加命令行参数--browser、--host'''
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser option: firefox or chrome"
             )
    # 添加host参数，设置默认测试环境地址
    parser.addoption(
        "--host", action="store", default="https://192.168.1.123", help="test host->https://192.168.1.123"
    )

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#         report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)

def _capture_screenshot():
    '''
    截图保存为base64
    :return:
    '''
    return _driver.get_screenshot_as_base64()

@pytest.fixture(scope='session')
def driver(request):
    '''定义全局driver参数'''
    global _driver
    if _driver is None:
        name = request.config.getoption("--browser")
        if name == "firefox":
            _driver = webdriver.Firefox()
        elif name == "chrome":
            _driver = webdriver.Chrome()
        else:
            _driver = webdriver.Chrome()
        logger.info("正在启动浏览器，名称为：%s" % name)
        login(_driver)
    def fn():
        logger.info("\n当前功能所有case执行完毕，即将关闭浏览器！")
        _driver.quit()
    request.addfinalizer(fn)
    return _driver

@pytest.fixture(scope='session')
def host(request):
    '''全局host参数'''
    return request.config.getoption("--host")

# pytest-json报告自定义--自动运行
@pytest.fixture(scope='session', autouse=True)
def extra_json_environment(request):
    request.config._json_environment.append(('project', ini.get_value("system", "system")))
    request.config._json_environment.append(('url', ini.get_value("system", "url")))
    request.config._json_environment.append(('username', ini.get_value("system", "username")))
    request.config._json_environment.append(('password', ini.get_value("system", "password")))

# pytest-html报告自定义--自动运行
def pytest_configure(config):
    config._metadata['project'] = ini.get_value("system", "system")
    config._metadata['url'] = ini.get_value("system", "url")
    config._metadata['username' ] = ini.get_value("system", "username")
    config._metadata['password'] = ini.get_value("system", "password")