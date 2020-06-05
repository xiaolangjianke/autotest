"""
------------------------------------
@Time : 2019/12/26 14:28
@Auth : gaoxch
@File : SystemLog.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""

import logging
from logging import handlers
from config.config import LOG_DIR


class Log:
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename=LOG_DIR + "/ouoa.log", level='info', when='D', backCount=3,
                 fmt='%(asctime)s %(filename)s ----> %(funcName)s [line:%(lineno)d] %(levelname)s --------> %(message)s '):
        self.logger = logging.getLogger(filename)
        self.logger.handlers = []
        self.logger.removeHandler(self.logger.handlers)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        # 往控制台上输出
        # self.sh = logging.StreamHandler()
        # 设置控制台上显示的格式
        # self.sh.setFormatter(format_str)
        # self.logger.addHandler(sh)

        # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        # 设置文件里写入的格式
        self.th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                                    encoding='utf-8')
        self.th.setFormatter(format_str)
        # 把对象加到logger里
        self.logger.addHandler(self.th)

    def close_handle(self):
        self.logger.removeHandler(self.th)
        self.th.close()
        self.logger.removeHandler(self.sh)
        self.sh.close()

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    log = Log()
    log.get_log().info("xixi")
