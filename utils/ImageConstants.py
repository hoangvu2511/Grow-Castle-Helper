from utils.SingleTonImplement import SingleTonImplement


class ImageConstants(SingleTonImplement):
    def __init__(self):
        self._BASE_PATH = 'images/'
        self.START_IMAGE = self._BASE_PATH + 'image.png'
        self.TREE_IMAGE = self._BASE_PATH + 'tree.png'
        self.MIMIC_IMAGE = self._BASE_PATH + 'mimic.png'

        self.ICON_CLOSE = self._BASE_PATH + 'ic_close.png'

        self.TOWER_CLICKABLE = self._BASE_PATH + 'max_dimond_use_case2.png'
        self.MAX_DIMOND_CONDITION = self._BASE_PATH + 'max_dimond_use_case1.png'
        self.MAX_DIMOND_TARGET = self._BASE_PATH + 'max_dimond_use_case3.png'
        self.MAX_DIMOND_LEVEL_UP = self._BASE_PATH + 'max_dimond_use_case4.png'

        self.ICON_APP = self._BASE_PATH + 'ic_app.png'
        self.ICON_APP_2 = self._BASE_PATH + 'ic_app2.png'
