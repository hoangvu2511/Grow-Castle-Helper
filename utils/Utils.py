import time
from datetime import datetime
from threading import Thread
from typing import Callable

from utils.SingletonImplement import SingletonImplement
from utils.TypeAlias import Args, Kwargs


class Utils(SingletonImplement):
    def __init__(self, tag: str | None = None):
        self.tag: str = tag or "Utils"

    @staticmethod
    def wait(delay: float):
        time.sleep(delay)

    @staticmethod
    def getCurrentTime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message: str):
        print(self.getCurrentTime(), self.tag, message)

    @staticmethod
    def runOnAnotherThread(
        func: Callable[..., object] | None, *args: tuple[Args], **kwargs: Kwargs
    ) -> Thread:
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread

    @staticmethod
    def log(message: str, tag: str | None = None):
        Utils(tag=tag).log(message)