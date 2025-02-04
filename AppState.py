from usecase.BattleUseCase import BattleUseCase
from usecase.MaxDimondUseCase import MaxDimondUseCase
from usecase.OpenAppUseCase import OpenAppUseCase
from utils.Utils import Utils


class AppState:

    def __init__(self, enableClickTree=True):
        self._isRunning = False
        self.battleUseCase = BattleUseCase(enableClickTree = enableClickTree)
        self.maxDimondUseCase = MaxDimondUseCase()
        self.openAppUseCase = OpenAppUseCase()

    def performStart(self):
        if not self.openAppUseCase.startWithRetry(retry=3):
            return
        Utils.wait(2)
        while True:
            if not self.battleUseCase.start_use_case():
                Utils.wait(0.5)
                continue
            self.maxDimondUseCase.start_use_case()
