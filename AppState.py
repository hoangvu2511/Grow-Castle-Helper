from usecase.BattleDungeon import BattleDungeon
from usecase.BattleUseCase import BattleUseCase
from usecase.MaxDimondUseCase import MaxDimondUseCase
from usecase.OpenAppUseCase import OpenAppUseCase
from utils.Utils import Utils


class AppState:

    def __init__(self, **kwargs):
        self._isRunning = False
        self.battleUseCase = BattleUseCase(enableClickTree=kwargs.get('enableClickTree', True))
        self.maxDimondUseCase = MaxDimondUseCase()
        self.openAppUseCase = OpenAppUseCase()
        self.battleDungeon = BattleDungeon(**kwargs)

    def performStart(self):
        if not self.checkApp():
            return
        Utils.wait(2)
        while True:
            if not self.battleUseCase.start_use_case():
                Utils.wait(0.5)
                continue
            self.maxDimondUseCase.start_use_case()

    def performDungeon(self):
        if not self.checkApp():
            return
        while True:
            self.battleDungeon.start_use_case()
            Utils.wait(2)

    def checkApp(self):
        return self.openAppUseCase.startWithRetry(retry=3)
