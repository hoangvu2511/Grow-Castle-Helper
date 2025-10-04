from PySide6.QtWidgets import QCheckBox

from usecase.BaseUsecase import BaseUseCase


class CheckBox:
    def __init__(
            self,
            text: str,
            checked: bool = True,
            useCase: BaseUseCase | None = None,
    ):
        self._view: QCheckBox = QCheckBox(text)
        self._view.setChecked(checked)
        self.useCase: BaseUseCase | None = useCase

    def initView(self) -> QCheckBox:
        return self._view

    def isEnabled(self) -> bool:
        return self._view.isChecked()
