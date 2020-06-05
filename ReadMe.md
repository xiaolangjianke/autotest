[TOC]

# 框架说明

## 文件夹结构

```
PyTest_Template
    │
    ├── run.py                  【运行文件，入口】
    ├── ReadMe.md               【说明文档】
    ├── Pipfile                 【pipenv环境安装文件】  
    ├── conftest.py	        【fixtrue】
    ├── Pipfile.lock
    ├── requirements.txt        【requirements环境安装文件】
    ├── config                  【配置文件】
    │       ├── config.ini      【元素，url、username、password】
    │       └── config.py     	【路径】     
    ├── report                  
    │       ├──  report.html    【html报告】
    │       └──  report.json    【json报告】
    ├── log 
    │       ├── logs            【日志目录】
    │       └── Log.py          【生成日志】
    ├── file                    【Excel等文件】
│   │
    ├── image                   【图片路径】 
    │
    ├── locator                 【获取页面元素目录】
    │
    ├── page                    【case的流程目录】                 
    ├── common                  【通用】
    │       ├── page_common.py  【页面元素通用】
    │       ├── login.py        【登录】
    │       ├── base.py         【查找元素通用】
    │       ├── Operation.py    【元素操作类，继承Base】
    │       └── driver.py       【driver生成，调试用】
    ├── page                    
    │       ├── Base_Page.py	【页面通过方法】  
    │── ****Page.py	        【页面独有元素与流程】
    ├── procedure               
    │       └── pro_***.py	【流程步骤】
    └── case                    
        └── test_***.py		【测试用例】
```
## conftest
所有case执行前后置条件
## case/conftest  
每条case执行前后置条件

## utils 工具包

### clipboard 
 
剪贴板，用于对键盘粘贴进行测试  
1）get_text：获取剪贴板内容  
2）set_text：设置剪贴板内容

### keyboard
键盘操作  
1）key_down：按下键  
2）key_up：抬起键  
3）one_key：模拟单个按键  
4）two_keys：模拟组合按键  

### parseConFile
读取元素配置文件  
get_all_sections：获取所有section  
get_all_options：获取所有option  
get_locators_or_account：获取指定的option  
get_option_value：获取指定section下所有的option  
### sendMailForReprot
发送邮件

## report 测试报告

测试报告

## page 页面  

### BasePage  

通用的页面操作

### page_object/****Page

页面元素获取与流程执行以及特殊的操作

## log 日志  

dir log：存储日志文件的目录  
Log：存储日志代码

## data 数据  

通过Excel工具类获取case的用例数据

## config 配置文件（元素、常量）

config_ini：存储定位元素数据、url、用户名、密码等固定数据
config.py：存储路径数据，为测试报告、执行路径等提供

## common 通用方法

通用方法，如：login前置条件

## case 测试用例  

## 编写case步骤

### 第一步：录入页面元素至config.ini文件中
格式：  
```ini
[模块名1] # 唯一

key1=value1

key2=value2

key3=value3

[模块名2] 

key1=value1

key2=value2

key3=value3

...

```
### 第二步，读取元素（Locators目录）

```python
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

```
### 第三步，创建page操作  

1)、创建***Page.py  
2)、继承pagebase  
3)、编写特有的操作代码（若有）  
4)、根据流程整合代码  

```python
from Locators.LoginLocaltors import login_localtors as ll
from page.BasePage import BasePage


class LoginPage(BasePage):

    def login_system02(self, username, password):
        # 登录操作
        self.send_keys(*ll.username, username)
        self.send_keys(*ll.password, password)
        self.click(*ll.button)
        # 获取登录失败系统提示
        text = self.get_element_text(*ll.tooltip)
        # 获取title
        title = self.get_title()
        return

```
## 第四步，准备测试数据  

此处的数据不是造数据，而是录入或者读取excel中的数据
```python
from utils.ExcelUtils import ExcelUtils


class TestData(object):

    login = ExcelUtils(index="Sheet1").get_data()
    login_data = ExcelUtils(index="login_data").get_data()

```


### 第五步 编写case，执行 

```python

import time
import pytest
from log.Log import Log
from data.TestData import login_data
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

    @pytest.mark.parametrize('username,password,repassword,name,phone,expect', login_data)
    def test_user(self, username, password, repassword, name, phone, expect):
        time.sleep(2)
        assert expect in "xixi","执行失败"
```

通过数据、page写测试类，执行