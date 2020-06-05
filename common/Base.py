from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from log.Log import Log

loc_dialog = ("class name", "ivu-message")


class Base():
    '''基于原生的selenium做二次封装'''

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5
        user = Log()
        self.log = user.get_log()

    def findElement(self, locator):
        ''' 查找元素，返回定位元素对象'''
        if not isinstance(locator, tuple):
            self.log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            self.log.info("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self, locator):
        ''' 查找元素列表，返回通过定位元素对位到的对象列表，返回list'''
        if not isinstance(locator, tuple):
            self.log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                self.log.info("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
                return eles
            except:
                return []

    def sendKeys(self, locator, text=''):
        '''输入文本内容，默认为空'''
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ''' 点击操作'''
        ele = self.findElement(locator)
        ele.click()

    def click_pop(self, locator, index):
        '''返回一组数组，通过索引定位'''
        ele = self.findElements(locator).pop(index)
        ele.click()

    def clear(self, locator):
        ''' 清楚文本框中的内容'''
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self, locator):
        '''判断元素是否被选中，返回bool值,不常用，现在的下拉列表多采用list形式'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        '''判断元素是否存在
            存在：返回true
            不存在：返回false
        '''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def element_in_or_no(self, locator, timeout=10):
        '''判断元素是否存在，
        存在：返回True
        不存在：返回false
        '''
        try:
            WebDriverWait(self.driver, timeout, 10).until(lambda x: x.find_element(*locator))
            return True
        except:
            return False

    def isElementExist2(self, locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            self.log.info("定位到元素的个数：%s" % n)
            return True

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def is_title_equal(self, _title=''):
        '''
        判断当前页面的title是否完全等于（==）预期字符串，
        相等：true
        不相等：false
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title=''):
        '''
        判断当前页面的title是否包含预期字符串，
        相等，返回true，不相等返回false
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text=''):
        '''判断某个元素中的text是否 包含 了预期的字符串，返回bool值'''
        if not isinstance(locator, tuple):
            self.log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value=''):
        '''判断某个元素中的value属性是否 包含 了预期的字符串，返回bool值, value为空字符串，返回Fasle'''
        if not isinstance(locator, tuple):
            self.log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def get_attribute(self, locator, name):
        '''获取属性，不常用'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            self.log.info("获取%s属性失败，返回'' " % name)
            return ""

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        '''通过索引,index是索引第几个，从0开始，默认选第一个'''
        element = self.findElement(locator)  # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        # 现在的下拉列表多采用list列表，selcet标签相对较少
        '''通过value属性，选中选项'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        # 切换嵌套内的不同html
        '''切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to_frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to_frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to_frame(ele)
        except:
            self.log.info("iframe切换异常")

    def switch_handle(self, window_name):
        ''' 切换tab页'''
        self.driver.switch_to_window(window_name)

    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    # 查询出所有符合定位方式（一般是xpath）的元素，通过下标进行选择，默认从0开始
    def sendKeys_pop(self, locator, text, index):
        '''返回一组数组，通过索引定位'''
        ele = self.findElements(locator).pop(index)
        ele.send_keys(text)

    def clear_pop(self, locator, index):
        '''返回一组数组，通过索引定位'''
        ele = self.findElements(locator).pop(index)
        ele.clear()

    def clear_and_sendkey_pop(self, locator, text, index):
        '''返回一组数组，通过索引定位'''
        ele = self.findElements(locator).pop(index)
        ele.clear()
        ele.send_keys(text)

    def click_and_sendkey_pop(self, locator, text, index):
        ele = self.findElements(locator).pop(index)
        ele.click()
        ele.send_keys(text)
