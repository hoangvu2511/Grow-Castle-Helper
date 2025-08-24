from ClickObject import ClickObject
from usecase.BaseUsecase import BaseUseCase
from utils.ImageConstants import ImageConstants


class BattleDungeon(BaseUseCase):
    defaultLevel = 'green_dragon'
    defaultHandleResult = 'get'

    def __init__(self, **kwargs):
        """init BattleDungeon
        Args:
            kwargs: settings
                levelSelected (str): level to be selected, default: green_dragon
                handleResult (str): handle result, default: get
        """
        super().__init__(**kwargs)
        imageConstants = ImageConstants()
        related = imageConstants.dungeonRelated()
        levelSelected = self._settings.get('levelSelected', self.defaultLevel)
        handleResult = self._settings.get('handleResult', self.defaultHandleResult)
        self.openDungeon = ClickObject(
            imageConstants.DUNGEON_ENTRY,
            icon_name="icon dungeon",
            enable_use_last=True,
        )
        self.levelSelected = ClickObject(
            related.get(levelSelected, self.defaultLevel),
            icon_name="icon level",
            enable_use_last=True,
        )
        self.startDungeon = ClickObject(
            related['battle_entry'],
            icon_name="icon battle",
            enable_use_last=True,
        )
        self.resultBtn = ClickObject(
            related.get(handleResult, self.defaultHandleResult),
            icon_name="icon result",
            numberOfClick=handleResult == 'mat' and 2 or 1,
            enable_use_last=True,
        )

    def start_use_case(self, **kwargs) -> bool:
        if not self.openDungeon.click():
            return False
        self._wait(2)
        if not self.levelSelected.click():
            self.clearAllOpenedPopUp()
            return False
        self._wait(2)
        if not self.startDungeon.click():
            self.clearAllOpenedPopUp()
            return False
        while True:
            if self.startDungeon.isExist(logError=False):
                break
            boxHandleResult = self.resultBtn.isExist(logError=False)
            if boxHandleResult:
                self.resultBtn.click()
                break
            self._wait(2)

        return True
