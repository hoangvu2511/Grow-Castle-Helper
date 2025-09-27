import os
from this import s
from typing_extensions import override
import pyautogui
from typing import Any
from pyscreeze import Box
from utils.Utils import Utils


class ClickObject:

    def __init__(self, path: str, **kwargs):
        """init ClickObject
        Args:
            path (str): path to the image need to be clicked
            kwargs: other settings
                confidence (float): confidence of the image, default: 0.8
                oneTimeClick (bool): if True, the object will be clicked only once
                logErrorOnClick (bool): if True, the error will be logged when the object is not found
                                        if False, the error will be ignored
                                        default: True
                logOnFound (bool): if True, the object will be logged when it is found
                                if False, the object will be ignored
                                default: False
                icon_name (str): name of the object for logging
                                default: path
                numberOfClick (int): number of click, default: 1
        """
        self._isValidatePath(path)
        self._path: str = path
        self._otherSettings: dict[str, Any] = kwargs
        self._isClicked: bool = False
        self._count_miss_match: int = 0
        self._enable_use_last: bool = self._otherSettings.get('enable_use_last', False)
        self._lastAction: (Box | None) = None
        self._confidence: float = self._otherSettings.get('confidence', 0.8)
        Utils().log(f'Created {path} {self._otherSettings}')

    @override
    def __str__(self) -> str:
        return self._otherSettings.get("icon_name", self._path).split('/')[-1]

    @staticmethod
    def _isValidatePath(path: str):
        assert path is not None, 'Path must not be None'
        assert isinstance(path, str), 'Path must be string'
        assert path.strip() != '', 'Path must not empty'
        assert os.path.exists(path), 'Path not found'

    def isExist(self, logError: bool=True) -> (Box | None):
        try:
            return pyautogui.locateOnScreen(
                image=self._path,
                confidence=self._confidence,
                grayscale=True,
                region=self._lastAction
            )
        except pyautogui.ImageNotFoundException:
            if logError:
                self._count_miss_match += 1
                Utils().log(
                    f'Not found {self} with path {self._path}, confidence: {self._confidence}, times: {self._count_miss_match}')
            return None

    def click(self) -> bool:
        oneTimeClick = self._otherSettings.get('oneTimeClick', False)
        if self._isClicked and oneTimeClick:
            return True
        try:
            action = self._retrieveAction()
            if not action: return False
            if self._otherSettings.get('logOnFound'):
                Utils().log(f'Found object at place {action}')
            numberOfClick = self._otherSettings.get('numberOfClick', 1)
            for _ in range(numberOfClick):
                pyautogui.click(action)
            if oneTimeClick:
                self._isClicked = True
            return True
        except Exception as e:
            self._lastAction = None
            Utils().log(f'Failed to click {self}: {e}')
            pass
        return False

    def _retrieveAction(self) -> Box | None:
        try:
            if self._lastAction is not None and self._enable_use_last:
                action = self._lastAction
            else:
                action = self.isExist(self._otherSettings.get('logErrorOnClick', True))
                if not action: return None
                self._lastAction = action
                Utils().log(f'Found action for {self._path}: {action}')
            return action
        except Exception as e:
            self._lastAction = None
            Utils().log(f'Failed to retrieve action for {self}: {e}')
            pass
        return None

    def reset(self):
        self._isClicked = False
