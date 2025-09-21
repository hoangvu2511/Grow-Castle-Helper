import sys
import threading

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QRadioButton,
    QComboBox, QHBoxLayout
)

from AppState import AppState
from utils.Utils import Utils


class AppWidget(QMainWindow):

    @staticmethod
    def openApp():
        app = QApplication(sys.argv)
        window = AppWidget()
        window.show()
        sys.exit(app.exec())

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button GUI")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add components
        self._battleUseCase(layout)
        self._dungeonUseCase(layout)

        self._startBtn(layout)
        self._appState = None

    def _battleUseCase(self, layout: QVBoxLayout):
        self.radio_1 = QRadioButton("Endless Battle")
        self.radio_1.setChecked(True)
        layout.addWidget(self.radio_1)

    def _dungeonUseCase(self, layout: QVBoxLayout):
        self.radio_2 = QRadioButton("Endless Dungeon")
        self.dropdown = QComboBox()
        self.dropdown.addItems(
            [
                'green_dragon',
                'black_dragon',
                'red_dragon',
                'sin',
                'legendary_dragon',
                'bone_dragon',

                'beginner_dungeon',
                'inter_dungeon',
                'expert_dungeon',
            ]
        )
        self.dropdown.setCurrentIndex(3)
        self.handleResult = QComboBox()
        self.handleResult.addItems(
            [
                'get',
                'mat',
            ]
        )
        self.handleResult.setCurrentIndex(0)
        layout.addWidget(self.radio_2)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.handleResult)

    def _startBtn(self, layout: QVBoxLayout):
        row = QHBoxLayout()

        startBtn = QPushButton("Start")
        startBtn.clicked.connect(self._onClickStart)
        row.addWidget(startBtn)

        stopBtn = QPushButton("Stop")
        stopBtn.clicked.connect(self._onClickStop)
        row.addWidget(stopBtn)
        self.currentThread = None
        layout.addLayout(row)

    def _onClickStart(self):
        settings = {
            'enableClickTree': False,
            'enableMaxDimond': False,
            'levelSelected': str(self.dropdown.currentText()),
            'handleResult': str(self.handleResult.currentText()),
        }
        action = None

        if self._appState is None:
            self._appState = AppState(**settings)

        if self.radio_1.isChecked():
            action = self._appState.performStart

        elif self.radio_2.isChecked():
            action = self._appState.performDungeon

        self.stop_event = threading.Event()
        self.currentThread = Utils.runOnAnotherThread(action, stop_event=self.stop_event)

    def _onClickStop(self):
        if not self.currentThread:
            return
        Utils().log('Stopping thread')
        self.stop_event.set()
        pass
