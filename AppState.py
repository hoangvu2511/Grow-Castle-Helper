from usecase.BattleDungeon import BattleDungeon
from usecase.BattleUseCase import BattleUseCase
from usecase.MaxDimondUseCase import MaxDimondUseCase
from usecase.OpenAppUseCase import OpenAppUseCase
from utils.Utils import Utils


class AppState:

    def __init__(self, **kwargs):
        self._isRunning = False
        self.battleUseCase = BattleUseCase(**kwargs)
        self.maxDimondUseCase = MaxDimondUseCase(**kwargs)
        self.openAppUseCase = OpenAppUseCase()
        self.battleDungeon = BattleDungeon(**kwargs)

    def performStart(self, stop_event=None):
        Utils.wait(2)
        while stop_event == None or (stop_event != None and stop_event.is_set() is False):
            if not self.battleUseCase.start_use_case(stop_event=stop_event):
                Utils.wait(0.5)
                continue
            self.maxDimondUseCase.start_use_case()

    def performDungeon(self, stop_event=None):
        while stop_event == None or (stop_event != None and stop_event.is_set() is False):
            self.battleDungeon.start_use_case()
            Utils.wait(2)

    def checkApp(self):
        return self.openAppUseCase.startWithRetry(retry=3)
