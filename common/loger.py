# #-*-coding:utf-8-*-
import os
from loguru import logger
from common.path import log


LOG_FILE = os.path.join(log, "test.log")
logger.add(sink=LOG_FILE, mode='a', rotation='100kb',backtrace=True ,retention='2 day',
           compression='zip',enqueue=True)
"""
roation :新增日志时间/日志大小
retention：删除时间
compression ：压缩方式
delay：延迟是否立即删除
"""


if __name__ == '__main__':
    logger.info("hello, world!")
    logger.debug('测试一下')  # 直接调用方法即可
    logger.error('错误测试')
