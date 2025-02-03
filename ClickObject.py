import pyautogui
from pyscreeze import Box
from utils.Utils import Utils
import traceback
import os

class ClickObject:

    
    def __init__(self, path: str, **kwargs): 
        """init ClickObject
        Args:
            path (str): path to the image need to be clicked
            kwargs (dict): other settings
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
        """
        self._isValidatePath(path)
        self._path = path
        self._otherSettings = kwargs
        self._isClicked = False

    def __str__(self):
        return self._otherSettings.get("icon_name", self._path).split('/')[-1]

    @staticmethod
    def _isValidatePath(path: str):
        assert path is not None, 'Path must not be None'
        assert isinstance(path, str), 'Path must be string'
        assert path.strip() != '', 'Path must not empty'
        assert os.path.exists(path), 'Path not found'

    def isExist(self, logError=True) -> (Box | None):
        confidence = self._otherSettings.get('confidence', 0.8)
        try:
            return pyautogui.locateOnScreen(self._path, confidence=confidence)
        except:
            if logError:
                Utils().log(f'Not found {self} with path {self._path}, confidence: {confidence}')
            return None

    def click(self):
        oneTimeClick = self._otherSettings.get('oneTimeClick')
        if self._isClicked and oneTimeClick:
            return True
        try:
            action = self.isExist(self._otherSettings.get('logErrorOnClick', True))
            if action:
                if self._otherSettings.get('logOnFound'):
                    Utils().log(f'Found object at place {action}')
                pyautogui.click(action)
                if oneTimeClick:
                    self._isClicked = True
                return True
        except:
            Utils().log(f'Failed to click {self}')
            pass
        return False

    def reset(self):
        self._isClicked = False
