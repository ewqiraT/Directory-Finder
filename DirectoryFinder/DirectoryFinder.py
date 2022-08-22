import os
import sys
from PyQt5.QtWidgets import *

import Directoryui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Directoryui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter = 0
        self.list_dirs = []
        self.setWindowTitle('Directory List')

        self.ui.pushButtonList.clicked.connect(self.pushButtonListHandler)
        self.ui.pushButtonNext.clicked.connect(self.pushButtonNextHandler)
        self.ui.pushButtonPrev.clicked.connect(self.pushButtonPrevHandler)
        self.ui.pushButtonFirst.clicked.connect(self.pushButtonFirstHandler)
        self.ui.pushButtonLast.clicked.connect(self.pushButtonLastHandler)
        self.ui.lineEditDir.setPlaceholderText('Enter full path')

    def pushButtonListHandler(self):
        path = self.ui.lineEditDir.text()
        try:
            dentries = os.scandir(path)
            dir_list = []
            for de in dentries:
                if de.is_dir():
                    dir_list.append(de.name)
            self.list_dirs = dir_list[::]
            dir_list.clear()
            self.ui.lineEditFileName.setText(self.list_dirs[0])
            self.counter = 0
            length_text = rf'{self.ui.lineEditDir.text()}\{self.ui.lineEditFileName.text()}'
            self.ui.lineEditLenght.setText(str(os.path.getsize(length_text)))
        except:
            print('Not avalieble directory')


    def pushButtonNextHandler(self):
        try:
            if len(self.list_dirs) - 1 > self.counter:
                self.counter += 1
            self.ui.lineEditFileName.setText(self.list_dirs[self.counter])
            length_text = rf'{self.ui.lineEditDir.text()}\{self.ui.lineEditFileName.text()}'
            self.ui.lineEditLenght.setText(str(os.path.getsize(length_text)))
        except:
            print('List except')


    def pushButtonPrevHandler(self):
        try:
            if self.counter > 0:
                self.counter -= 1
            self.ui.lineEditFileName.setText(self.list_dirs[self.counter])
            length_text = rf'{self.ui.lineEditDir.text()}\{self.ui.lineEditFileName.text()}'
            self.ui.lineEditLenght.setText(str(os.path.getsize(length_text)))
        except:
            print('List except')


    def pushButtonFirstHandler(self):
        try:
            self.ui.lineEditFileName.setText(self.list_dirs[0])
            length_text = rf'{self.ui.lineEditDir.text()}\{self.ui.lineEditFileName.text()}'
            self.ui.lineEditLenght.setText(str(os.path.getsize(length_text)))
        except:
            pass


    def pushButtonLastHandler(self):
        try:
            self.ui.lineEditFileName.setText(self.list_dirs[len(self.list_dirs) - 1])
            length_text = rf'{self.ui.lineEditDir.text()}\{self.ui.lineEditFileName.text()}'
            self.ui.lineEditLenght.setText(str(os.path.getsize(length_text)))
        except:
            pass


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()