import sys
import threading
import os
from typing import Callable
from xmlrpc.client import Boolean

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QRadioButton,
    QComboBox, QHBoxLayout, QTextEdit
)
from PySide6.QtCore import Signal, Slot

from AppState import AppState
from utils.Utils import Utils


class AppWidget(QMainWindow):
    _log_signal = Signal(str)
    instance: 'AppWidget | None' = None

    @staticmethod
    def openApp():
        app = QApplication(sys.argv)
        window = AppWidget()
        window.show()
        sys.exit(app.exec())

    def __init__(self):
        super().__init__()
        AppWidget.instance = self
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
        
        # Log Viewer
        self._logViewer = QTextEdit()
        self._logViewer.setReadOnly(True)
        self._logViewer.setMinimumHeight(100)
        self._logViewer.setMaximumHeight(200)
        layout.addWidget(self._logViewer)
        
        self._log_signal.connect(self._append_log)
        # Utils().setLogCallback(self._receive_log)

        self._appState: AppState | None = None
        self._resultPrinted: Boolean = False

    def _receive_log(self, message: str):
        self._log_signal.emit(message)

    @Slot(str)
    def _append_log(self, message: str):
        self._logViewer.append(message)


    def _battleUseCase(self, layout: QVBoxLayout):
        self._radio_1: QRadioButton = QRadioButton("Endless Battle")
        self._radio_1.setChecked(True)
        layout.addWidget(self._radio_1)

    def _dungeonUseCase(self, layout: QVBoxLayout):
        self._radio_2: QRadioButton = QRadioButton("Endless Dungeon")
        self._dropdown: QComboBox = QComboBox()
        self._dropdown.addItems(
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
        self._dropdown.setCurrentIndex(3)
        self._handleResult: QComboBox = QComboBox()
        self._handleResult.addItems(
            [
                'get',
                'mat',
            ]
        )
        self._handleResult.setCurrentIndex(0)
        layout.addWidget(self._radio_2)
        layout.addWidget(self._dropdown)
        layout.addWidget(self._handleResult)

    def _startBtn(self, layout: QVBoxLayout):
        row = QHBoxLayout()

        startBtn = QPushButton("Start")
        _ = startBtn.clicked.connect(self._onClickStart)
        row.addWidget(startBtn)

        stopBtn = QPushButton("Stop")
        _ = stopBtn.clicked.connect(self._onClickStop)
        row.addWidget(stopBtn)
        self._currentThread = None
        layout.addLayout(row)

    def _onClickStart(self):
        settings = {
            'enableClickTree': False,
            'enableMaxDimond': False,
            'levelSelected': str(self._dropdown.currentText()),
            'handleResult': str(self._handleResult.currentText()),
            'isBattle': self._radio_1.isChecked(),
        }
        action: Callable[..., object] | None = None

        if self._appState is None:
            self._appState = AppState(**settings)

        if self._radio_1.isChecked():
            action = self._appState.performStart

        elif self._radio_2.isChecked():
            action = self._appState.performDungeon

        self._stop_event: threading.Event = threading.Event()
        self._currentThread: threading.Thread | None = Utils.runOnAnotherThread(action, stop_event=self._stop_event)
        self._resultPrinted = False

    def _onClickStop(self):
        if not self._currentThread:
            return
        Utils().log('Stopping thread')
        self._stop_event.set()
        self._printResultLog()

    def _printResultLog(self):
        if self._resultPrinted:
            return
        self._appState.printResultLog()
        self._resultPrinted = True
