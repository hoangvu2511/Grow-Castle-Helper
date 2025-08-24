import time
from datetime import datetime
from threading import Thread

from utils.SingletonImplement import SingletonImplement


class Utils(SingletonImplement):

    def __init__(self, tag=None):
        self.tag = tag or 'Utils'

    @staticmethod
    def wait(delay):
        time.sleep(delay)

    @staticmethod
    def getCurrentTime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message):
        print(self.getCurrentTime(), self.tag, message)

    @staticmethod
    def runOnAnotherThread(func, *args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
