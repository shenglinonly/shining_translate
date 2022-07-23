from PyQt5 import uic
from translates import translate as trans
from threading import Thread


class Stats:
    def __init__(self):
        self.ui = uic.loadUi("ui\\translate.ui")
        self.ui.pushButton.clicked.connect(self.translate)
        self.ui.pushButton_2.clicked.connect(self.remove)
        # self.trans = trans(self.trans_text)

    def translate(self):
        def run():
            trans_text = self.ui.textEdit.toPlainText()
            trans_result = trans(trans_text)
            return trans_result
        thread = Thread(target=run)
        thread.start()
        self.ui.textEdit_2.setPlainText(run())

    def remove(self):
        self.ui.textEdit_2.setPlainText('')
        self.ui.textEdit.setPlainText('')



