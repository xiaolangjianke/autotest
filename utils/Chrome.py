from selenium import webdriver
from log.user_log import UserLog


'''
传参则为headless模式，即不开浏览器

不传参数则为打开浏览器
'''

def Chrome(is_display=None):
    log = UserLog()
    loger = log.get_log()
    loger.info("\n打开浏览器")
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    if is_display == None:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    return driver