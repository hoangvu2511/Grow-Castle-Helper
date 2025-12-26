from typing_extensions import override
from ClickObject import ClickObject
from usecase.BaseUsecase import BaseUseCase
from utils.ImageConstants import ImageConstants
from utils.TypeAlias import Args, Kwargs
from utils.Utils import Utils

class BattleUseCase(BaseUseCase):
    def __init__(self, **kwargs: Kwargs):
        super().__init__(**kwargs)
        imageConstants = ImageConstants()
        self.btn: ClickObject = ClickObject(
            imageConstants.START_IMAGE, icon_name="icon battle", enable_use_last=True
        )
        self.close_btn: ClickObject = ClickObject(
            imageConstants.ICON_CLOSE, icon_name="icon close", enable_use_last=True
        )
        self._buffAction = [
            ClickObject(
                imageConstants.MIMIC_IMAGE,
                logErrorOnClick=False,
                logOnFound=False,
                enable_use_last=False,
                confidence=0.75,
            ),
        ]
        if self._settings.get("enableClickTree", True):
            self._buffAction.append(
                ClickObject(imageConstants.GOLD_IMAGE, oneTimeClick=True)
            )

    @override
    def start_use_case(self, *args: Args, **kwargs: Kwargs):
        stop_event = kwargs.get("stop_event")
        if not self.btn.click():
            return False
        Utils.wait(2)
        while not self.isExist() and (
            stop_event == None or (stop_event != None and stop_event.is_set() is False)
        ):
            screen = self.capture_screen()
            for action in self._buffAction:
                Utils.wait(0.1)
                action.click(haystackImage=screen)
        self.reset()
        return True

    @override
    def isExist(self):
        return self.btn.isExist(logError=False) != None

    @override
    def reset(self):
        for action in self._buffAction:
            action.reset()

    @override
    def logFinalResult(self):
        startBattleClickTimes = self.btn.getSuccessClickTimes()
        mimicClickTimes = self._buffAction[0].getSuccessClickTimes()
        _utils = Utils(tag="Battle", console_log=True)
        _utils.log("=========Battle result==========")
        _utils.log(f"Start battle click times: {startBattleClickTimes} => {startBattleClickTimes} waves")
        _utils.log(f"Mimic click times: {mimicClickTimes}")