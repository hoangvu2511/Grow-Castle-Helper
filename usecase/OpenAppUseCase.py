from utils.ImageConstants import ImageConstants
from utils.Utils import Utils
from usecase.BaseUsecase import BaseUseCase
from ClickObject import ClickObject

class OpenAppUseCase(BaseUseCase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        imageContants = ImageConstants()
        defaultConfidence = 0.85
        self._listBtn = [
            ClickObject(imageContants.ICON_APP, logOnFound = True, confidence = defaultConfidence, icon_name="app icon"),
            ClickObject(imageContants.ICON_APP_2, logOnFound = True, confidence = defaultConfidence, icon_name="alternative app icon"),
        ]

    def startWithRetry(self, **kwargs) -> bool:
        result = super().startWithRetry(**kwargs)
        if not result:
            Utils().log('Could not open app.')
        return result

    def start_use_case(self, **kwargs) -> bool:
        result = False
        for btn in self._listBtn:
            result = btn.click()
            if result: break
            else: Utils.wait(1)
        return result
