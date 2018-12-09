#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets
from Main_win import Ui_MainWindow

class MyPyQT_Form(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def Open_File(self):
        self.textEdit.setText("你点击了按钮")
    def Enlarge(self):
        self.textEdit.setText("你点击了按钮")
    def lessen(self):
        self.textEdit.setText("你点击了按钮")
    def Ctreate_Labels(self):
        self.textEdit.setText("你点击了按钮")
    def Change_Labels(self):
        self.textEdit.setText("你点击了按钮")
    def Undo_toPrev(self):
        self.textEdit.setText("你点击了按钮")
    def Save_File(self):
        self.textEdit.setText("你点击了按钮")
    def Main_DisplayWin(self):
        self.textEdit.setText("你点击了按钮")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
