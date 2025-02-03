import time
from datetime import datetime

from utils.SingleTonImplement import SingleTonImplement


class Utils(SingleTonImplement):

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
