from usecase.BaseUsecase import BaseUseCase
from utils.ImageConstants import ImageConstants
from ClickObject import ClickObject
from utils.Utils import Utils

class MaxDimondUseCase(BaseUseCase):

    def __init__(self):
        imageConstant = ImageConstants()
        self._maxDimond = ClickObject(imageConstant.MAX_DIMOND_CONDITION, confidence=0.3, icon_name="'Max dimond condition'")
        self._maxDimondTarget = ClickObject(imageConstant.MAX_DIMOND_TARGET)
        self._maxDimondLevelUp = ClickObject(imageConstant.MAX_DIMOND_LEVEL_UP)
        self._tower = ClickObject(imageConstant.TOWER_CLICKABLE)
        self._ic_close = ClickObject(imageConstant.ICON_CLOSE, confidence=0.7)

    def start_use_case(self, **kwargs) -> bool:
        Utils.wait(2)
        if not self._maxDimond.isExist():
            return
        self._tower.click()
        Utils.wait(1)
        if not self._maxDimondTarget.click():
            return
        for i in range(60):
            self._maxDimondLevelUp.click()
            Utils.wait(0.2)
        self._ic_close.click()
        self._ic_close.click()
        return True
        