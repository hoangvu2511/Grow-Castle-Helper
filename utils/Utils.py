import time
from datetime import datetime
from threading import Thread
from typing import Callable

from utils.SingletonImplement import SingletonImplement
from utils.TypeAlias import Args, Kwargs


class Utils(SingletonImplement):
    def __init__(self, tag: str | None = None, **kwargs: Kwargs):
        if getattr(self, '_initialized', False):
            return
        self._initialized = True
        self.tag: str = tag or "Utils"
        self.log_callback: Callable[[str], None] | None = None
        self._print_console_log: bool = kwargs.get("console_log", False)
        try:
            from app.AppWidget import AppWidget
            if AppWidget.instance:
                self.setLogCallback(AppWidget.instance._receive_log)
        except ImportError:
            pass

    def setLogCallback(self, callback: Callable[[str], None]):
        self.log_callback = callback

    @staticmethod
    def wait(delay: float):
        time.sleep(delay)

    @staticmethod
    def getCurrentTime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message: str):
        log_msg = f"{self.getCurrentTime()} [{self.tag}] {message}"
        if self._print_console_log:
            print(log_msg)
        if self.log_callback:
            self.log_callback(log_msg)

    def log_result(self, message: str, tag: str | None = None) -> None:
        """Log a result message, always printing to console regardless of _print_console_log."""
        effective_tag = tag or self.tag
        log_msg = f"{self.getCurrentTime()} [{effective_tag}] {message}"
        print(log_msg)
        if self.log_callback:
            self.log_callback(log_msg)

    @staticmethod
    def runOnAnotherThread(
        func: Callable[..., object] | None, *args: tuple[Args], **kwargs: Kwargs
    ) -> Thread:
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread

    @staticmethod
    def logMsg(message: str, tag: str | None = None) -> None:
        Utils().log_result(message, tag=tag)
