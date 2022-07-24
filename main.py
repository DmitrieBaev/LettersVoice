""" main """

# base imports
import os, sys, asyncio
# 3-rd party libs
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QMessageBox,
                             QFileDialog)
# project modules
from ui.MainWindow import Ui_MainWindow
from core.settings import AVAILABLE_HANDLERS, AVAILABLE_FILTERS


class wndProc(QMainWindow):
    def __init__(self):
        super(wndProc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button event handlers
        # tab_1 handlers
        self.ui.btnPerform.clicked.connect(self.btnPerformClicked)
        self.ui.btnChooseFile.clicked.connect(self.btnChooseFileClicked_FileDialog)
        self.ui.btnChooseFolder.clicked.connect(self.btnChooseFolderClicked_FileDialog)
        # tab_2 handlers
        self.ui.btnMuteUnmute.clicked.connect(self.btnMuteUnmuteClicked)

# region DocumentSpeech_Tab
    def btnChooseFileClicked_FileDialog(self):
        self.ui.btnChooseFile.setText(
            QFileDialog.getOpenFileName(
                self,
                'Choose file ...',
                f'{os.path.dirname(__file__)}',
                filter=AVAILABLE_FILTERS
            )[0]
        )

    def btnChooseFolderClicked_FileDialog(self):
        self.ui.btnChooseFolder.setText(
            QFileDialog.getExistingDirectory(
                self,
                "Choose folder to save speech file ...",
                ".")
        )

    def btnPerformClicked(self):
        asyncio.run(self.main())

    async def main(self):
        async def get_handler(suffix: str):
            """Returns the desired handler corresponding to the file type or None.

            :param suffix: [String] File extension.
            :return: Document handler or None.
            """
            try:
                return AVAILABLE_HANDLERS[suffix]
            except KeyError as e:
                await self.showErrorMessage(f'Handler for {e} filetype is unavailable!')
                # ERRORS.append(f'[X] Handler for {e} filetype is unavailable!')
                return None

        async def check_paths() -> bool:
            if self.ui.btnChooseFile.text() == 'Choose file ...':
                await self.showErrorMessage(f'Path to file isn\'t chosen!')
                return False

            if self.ui.btnChooseFolder.text() == 'Choose folder to save speech file ...':
                await self.showErrorMessage(f'Path to folder isn\'t chosen!')
                return False

            return True

        if not await check_paths():
            return

        path2file_ = self.ui.btnChooseFile.text()
        path2folder_ = self.ui.btnChooseFolder.text()
        handler = await get_handler(os.path.splitext(path2file_)[1])

        if handler is None:
            return

        from handlers.SpeechHandler import TextSpeechHandler, SpeechSaver

        raw_content = await handler().convert(path2file_)
        raw_speech = await TextSpeechHandler().convert(raw_content,
                                                       language=self.ui.cmbSpeechLanguage_1.currentText())
        await SpeechSaver().save(raw_speech, path2folder=path2folder_)
        # await SpeechSaver().save(
        #     # Raw content:
        #     await TextSpeechHandler().convert(
        #         await handler().convert(path2file_),  # Raw speech.
        #         language=self.ui.cmbSpeechLanguage_1.currentText()  # Language from cmbBox.
        #     ),
        #     path2folder=path2folder_  # Path to folder.
        # )
# endregion

# region LiveSpeech_Tab
    def btnMuteUnmuteClicked(self):
        if self.ui.btnMuteUnmute.isChecked():
            # [!] MUTED = False
            self.ui.btnMuteUnmute.setIcon(self.ui.ICON_UNMUTED)
        else:
            # [!] MUTED = True
            self.ui.btnMuteUnmute.setIcon(self.ui.ICON_MUTED)
# endregion

    async def showErrorMessage(self, msg_text: str = ''):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(msg_text)
        msg.setWindowTitle("Error")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    application = wndProc()
    application.show()

    sys.exit(app.exec())
