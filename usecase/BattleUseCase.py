from typing_extensions import override
from ClickObject import ClickObject
from usecase.BaseUsecase import BaseUseCase
from utils.ImageConstants import ImageConstants
from utils.Utils import Utils


class BattleUseCase(BaseUseCase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        imageConstants = ImageConstants()
        self.btn = ClickObject(
            imageConstants.START_IMAGE,
            icon_name="icon battle",
            enable_use_last=True
        )
        self._buffAction = [
            ClickObject(imageConstants.MIMIC_IMAGE, logErrorOnClick=False, logOnFound=False, enable_use_last=False),
        ]
        if self._settings.get('enableClickTree', True):
            self._buffAction.append(ClickObject(imageConstants.GOLD_IMAGE, oneTimeClick=True))

    @override
    def start_use_case(self, *args, **kwargs):
        stop_event = kwargs.get('stop_event')
        if not self.btn.click():
            return False
        Utils.wait(2)
        while not self.isExist() and (stop_event == None or (stop_event != None and stop_event.is_set() is False)):
            for action in self._buffAction:
                Utils.wait(0.5)
                action.click()
        self.reset()
        return True

    @override
    def isExist(self):
        return self.btn.isExist(logError=False) != None

    @override
    def reset(self):
        for action in self._buffAction:
            action.reset()
