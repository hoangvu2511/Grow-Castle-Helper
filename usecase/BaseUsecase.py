import numbers
from abc import ABC, abstractmethod

from ClickObject import ClickObject
from utils.ImageConstants import ImageConstants
from utils.SingleTonImplement import SingleTonImplement
from utils.Utils import Utils


class BaseUseCase(SingleTonImplement, ABC):

    def __init__(self, **kwargs):
        self._settings = kwargs

    def _usecaseLog(self, message):
        Utils().log(f'{self.__class__.__name__}: {message}')

    def _wait(self, delay: numbers.Number):
        Utils.wait(delay)

    def startWithRetry(self, **kwargs) -> bool:
        """startWithRetry
        Args:
            **kwargs:
                retry (int): retry times, default: -1
        Returns:
            bool: True if success, False if failed
        """
        timeToRetry = kwargs.get('retry', -1)
        result = self.start_use_case(**kwargs)
        timeToRetry = timeToRetry - 1
        while not result and timeToRetry >= 0:
            self._usecaseLog(f'Retry left: {timeToRetry}')
            result = self.start_use_case(**kwargs)
            if result: break
            timeToRetry = timeToRetry - 1

        return result

    @abstractmethod
    def start_use_case(self, **kwargs) -> bool:
        return True

    def isExist(self) -> bool:
        return False

    def reset(self):
        pass

    def clearAllOpenedPopUp(self):
        icon_close = ClickObject(ImageConstants().ICON_CLOSE, confidence=0.7)
        while icon_close.click():
            Utils().wait(2)
