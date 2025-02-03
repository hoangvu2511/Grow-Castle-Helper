from utils.ImageConstants import ImageConstants
from ClickObject import ClickObject
from usecase.BaseUsecase import BaseUseCase
from utils.Utils import Utils


class BattleUseCase(BaseUseCase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        imageConstants = ImageConstants()
        self.btn = ClickObject(imageConstants.START_IMAGE, icon_name="icon battle")
        self._buffAction = [
            ClickObject(imageConstants.MIMIC_IMAGE, logErrorOnClick=False, logOnFound=False),
        ]
        if self._settings.get('enableClickTree', True):
            self._buffAction.append(ClickObject(imageConstants.TREE_IMAGE, oneTimeClick=True))

    def start_use_case(self, *args, **kwargs):
        if not self.btn.click():
            return False
        Utils.wait(2)
        while not self.isExist():
            for action in self._buffAction:
                Utils.wait(0.5)
                action.click()
        self.reset()
        return True

    def isExist(self):
        return self.btn.isExist(logError=False)

    def reset(self):
        for action in self._buffAction:
            action.reset()
