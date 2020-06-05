# !/usr/bin/python3
# coding=utf-8
import configparser
import os

'''
读取config.ini配置文件

'''
# 获取config.ini文件路径
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config/config.ini')


class Read_Ini():

    def __init__(self):
        self.cf = configparser.ConfigParser()  # 实例化
        self.cf.read(ini_path, encoding="utf-8-sig")  # 读取文件

    def get_value(self, section, key):
        ''' 通过模块（section)和字段（key)获取对应的定位元素 '''
        value = self.cf.get(section, key)
        return value


# if __name__ == '__main__':
#     a = Read_Ini()
#     value = a.get_value("system", "system")
#     print(value)
