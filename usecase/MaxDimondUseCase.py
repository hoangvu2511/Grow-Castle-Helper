from ClickObject import ClickObject
from usecase.BaseUsecase import BaseUseCase
from utils.ImageConstants import ImageConstants
from utils.Utils import Utils


class MaxDimondUseCase(BaseUseCase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        imageConstant = ImageConstants()
        self._maxDimond = ClickObject(imageConstant.MAX_DIMOND_CONDITION, confidence=0.5,
                                      icon_name="'Max dimond condition'")
        self._maxDimondTarget = ClickObject(imageConstant.MAX_DIMOND_TARGET)
        self._maxDimondLevelUp = ClickObject(imageConstant.MAX_DIMOND_LEVEL_UP, numberOfClick=15,
                                             icon_name="level up button")
        self._tower = ClickObject(imageConstant.TOWER_CLICKABLE)

    def start_use_case(self, **kwargs) -> bool:
        if not self._settings.get('enableMaxDimond', True):
            return False
        Utils.wait(3)
        if not self._maxDimond.isExist():
            return False
        self._tower.click()
        Utils.wait(1)
        if not self._maxDimondTarget.click():
            return False
        Utils.wait(1)
        self._maxDimondLevelUp.click()
        self.clearAllOpenedPopUp()
        return True
