"""
------------------------------------
@Time : 2019/12/19 14:58
@Auth : gaoxch  
@File : BasePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from log.Log import Log
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)
from utils.clipboard import ClipBoard
from utils.keyboard import KeyBoard
from utils.parseConFile import ParseConFile
from utils.ExcelUtils import ExcelUtils


class BasePage(object):
    """结合显示等待封装一些selenium内置方法"""

    def __init__(self, driver, timeout=10):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'css': By.CSS_SELECTOR
        }
        self.driver = driver
        self.outTime = timeout
        log = Log()
        self.loger = log.get_log()

    def find_element(self, by, locator):
        """
        find alone element
        :param by: eg: id, name, xpath, css.....
        :param locator: id, name, xpath for str
        :return: element object
        """
        try:
            self.loger.info('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            self.loger.info('error: found "{}" timeout!'.format(locator), t)
        else:
            return element

    def find_elements(self, by, locator):
        """
        find group elements
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: elements object
        """
        try:
            self.loger.info('[Info:start find the elements "{}" by "{}"!]'.format(locator, by))
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            self.loger.info('error: found "{}" timeout!'.format(locator), t)
        else:
            return elements

    def is_element_exist(self, by, locator):
        """
        assert element if exist
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: if element return True else return false
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                self.loger.info('Error: element "{}" not exist'.format(locator))
                return False
            return True
        else:
            self.loger.info('the "{}" error!'.format(by))

    def is_click(self, by, locator):
        '''
         判断元素是否可点击
        :param by: 元素定位方式
        :param locator: 元素定位置
        :return: 若可以点击，返回元素对象
        '''
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime). \
                    until(ec.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                self.loger.info("元素不可以点击")
            else:
                return element
        else:
            self.loger.info('the "{}" error!'.format(by))

    def send_keys(self, by, locator, value=None):
        '''
        先清楚对应元素已有的值，然后输入新的值
        :param by: 元素定位方式
        :param locator: 元素定位值
        :param value: 输入的值
        :return:
        '''
        self.loger.info('info:input "{}"'.format(value))
        try:
            element = self.find_element(by, locator)
            element.clear()
            element.send_keys(value)
        except AttributeError as e:
            self.loger.info(e)

    def clear(self, by, locator):
        '''
        清楚当前元素对应的数据
        :param by: 元素定位方式
        :param locator: 元素定位值
        :return:
        '''
        self.loger.info('info:clearing value')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            self.loger.info(e)

    def click(self, by, locator):
        '''
        先判断元素是否可点击，若可以点击，则点击
        若不可以点击，则抛出异常
        :param by:
        :param locator:
        :return:
        '''
        self.loger.info('info:click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element:
            element.click()
        else:
            self.loger.info('the "{}" unclickable!')

    def is_alert(self):
        '''
        assert alert if exsit
        :return:
        '''
        try:
            re = WD(self.driver, self.outTime).until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException):
            self.loger.info("error:no found alert")
        else:
            return re

    def load_url(self, url):
        '''
        记载新的url
        :param url:新的url
        :return:
        '''
        self.loger.info('info: string upload url "{}"'.format(url))
        self.driver.get(url)

    def switch_to_frame(self, by, locator):
        '''
        判断frame是否存在，存在就跳到frame
        :param by: 元素定位方式
        :param locator: 元素定位值
        :return:
        '''
        self.loger.info('info:switching to iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                self.loger.info('error: found "{}" timeout！切换frame失败'.format(locator), t)
        else:
            self.loger.info('the "{}" error!'.format(by))

    def switch_to_default_frame(self):
        '''
        返回默认的frame
        :return:
        '''
        self.loger.info('info:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            self.loger.info(e)

    def get_alert_text(self):
        '''
        获取alert的提示信息
        :return:
        '''
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None

    def get_element_text(self, by, locator):
        '''
        获取某一个元素的text信息
        :param by: 元素定位方式
        :param locator: 元素定位值
        :return: 元素对应的文本
        '''
        text=None
        try:
            element = self.find_element(by, locator)
            text = element.text

        except AttributeError:
            self.loger.info('get "{}" text failed return None'.format(locator))
        return text

    def get_source(self):
        '''
        获取页面源码
        :return:
        '''
        return self.driver.page_source

    def switch_tab(self, count):
        ''' 切换至第N个tab窗口 '''
        driver = self.driver
        handles = driver.window_handles
        driver.switch_to.window(handles[count - 1])

    def get_title(self):
        '''
        或html页面title
        :return: 标题名称
        '''
        driver = self.driver
        title = driver.title
        return title

    def click_and_click(self, *key):
        '''
        多点操作
        每传入一个元素，点击一次
        如：下拉选择、时间选择框、类型选择等
        :param key: 定位元素的list
        :return:
        '''
        for ele in key:
            self.click(*ele)
            sleep(0.5)

    @staticmethod
    def sleep(num=0):
        '''
        强制等待
        :param num:
        :return:
        '''
        print('info:sleep "{}" minutes'.format(num))
        sleep(num)

    def ctrl_v(self, value):
        '''
        ctrl + V 粘贴
        :param value: 待粘贴的值
        :return:
        '''
        self.loger.info('info:pasting "{}"'.format(value))
        ClipBoard.set_text(value)
        self.sleep(3)
        KeyBoard.two_keys('ctrl', 'v')

    @staticmethod
    def enter_key():
        '''
        键盘输入
        :return:
        '''
        print('info:keydown enter')
        KeyBoard.one_key('enter')

    def wait_element_to_be_located(self, by, locator):
        '''
        显示等待值
        :param by: 元素定位方式
        :param locator: 元素定位值
        :return:
        '''
        self.loger.info('info:waiting "{}" to be located'.format(locator))
        try:
            return WD(self.driver, self.outTime).until(ec.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            self.loger.info('error: found "{}" timeout！'.format(locator), t)

    def get_page_source(self):
        return self.get_source()

    def del_choose(self, *key, value):
        '''
        悬浮展示删除按钮-->点击删除原有数据-->输入的数据（模糊搜索/精准搜索）-->选择需要的数据
        :param ele1: 文本框的定位元素
        :param ele2: 删除点的定位元素
        :param ele3: 需要的数据内容的定位元素
        :param value:输入的值
        :return:
        '''
        self.move_to_element(*key[0])
        sleep(0.5)
        try:
            self.click(*key[1])
        except:
            self.loger.info("无数据，不需要删除")
        self.sendKeys(*key[0], value)
        sleep(0.5)
        self.click(*key[2])

    def move_to_element(self, by, locator):
        '''
        移动到指定元素位置
        :param by: 定位方式
        :param locator: 定位值
        :return:
        '''
        ele = self.find_element(by, locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def send_click(self,*key,value):
        '''
        输入-->点击操作
        :param key:元素同意格式
        :param value: 需要输入的值
        :return:
        '''
        self.send_keys(*key[0],value)
        self.click(*key[1])


if __name__ == '__main__':
    driver = 1
    a = BasePage(driver)
    ele1 = ("xpath", "//123")
    ele2 = ("xpath", "//456")
    ele3 = ("xpath", "//789")
    a.send_click(ele1,ele2,value="hehe")
    # a.send_keys(*ele1,value="text")
    # a.del_choose(ele1, ele2, ele3, value="hehe")
    # a.click_and_click(ele1,ele2,ele3)
    # a.send_keys(*ele1, value="呵呵")
