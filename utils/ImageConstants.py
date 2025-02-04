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

        self.DUNGEON_BASE = self._BASE_PATH + 'dungeon/'
        self.DUNGEON_ENTRY = f'{self.DUNGEON_BASE}dungeon_entry.png'

    def dungeonRelated(self) -> dict:
        base_result = f'{self.DUNGEON_BASE}result/'
        return {
            'battle_entry': f'{self.DUNGEON_BASE}battle_entry.png',
            'beginner_dungeon': f'{self.DUNGEON_BASE}beginner_dungeon.png',
            'black_dragon': f'{self.DUNGEON_BASE}black_dragon.png',
            'bone_dragon': f'{self.DUNGEON_BASE}bone_dragon.png',
            'expert_dungeon': f'{self.DUNGEON_BASE}expert_dungeon.png',
            'green_dragon': f'{self.DUNGEON_BASE}green_dragon.png',
            'inter_dungeon': f'{self.DUNGEON_BASE}inter_dungeon.png',
            'legendary_dragon': f'{self.DUNGEON_BASE}legendary_dragon.png',
            'red_dragon': f'{self.DUNGEON_BASE}red_dragon.png',
            'sin': f'{self.DUNGEON_BASE}sin.png',

            'get': f'{base_result}get.png',
            'mat': f'{base_result}mat.png',
            'sell': f'{base_result}sell.png',
        }
