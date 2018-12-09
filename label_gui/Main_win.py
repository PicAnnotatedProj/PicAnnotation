# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_win.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(10, 30, 71, 41))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(10, 80, 71, 41))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(10, 130, 71, 41))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(10, 180, 71, 41))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_5.setGeometry(QtCore.QRect(10, 230, 71, 41))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(10, 280, 71, 41))
        self.toolButton_6.setObjectName("toolButton_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 75, 51))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(90, 30, 531, 351))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 30, 160, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labellist = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.labellist.setObjectName("labellist")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.labellist.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labellist.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.labellist)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.labellist.setCurrentIndex(0)
        self.toolButton_2.pressed.connect(MainWindow.Open_File)
        self.toolButton.clicked.connect(MainWindow.Enlarge)
        self.toolButton_3.clicked.connect(MainWindow.lessen)
        self.toolButton_4.clicked.connect(MainWindow.Ctreate_Labels)
        self.toolButton_5.clicked.connect(MainWindow.Change_Labels)
        self.toolButton_6.clicked.connect(MainWindow.Undo_toPrev)
        self.pushButton.clicked.connect(MainWindow.Save_File)
        self.graphicsView.rubberBandChanged['QRect','QPointF','QPointF'].connect(MainWindow.Main_DisplayWin)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_2.setText(_translate("MainWindow", "打开"))
        self.toolButton.setText(_translate("MainWindow", "放大"))
        self.toolButton_3.setText(_translate("MainWindow", "缩小"))
        self.toolButton_4.setText(_translate("MainWindow", "创造标记"))
        self.toolButton_5.setText(_translate("MainWindow", "修改标记"))
        self.toolButton_6.setText(_translate("MainWindow", "撤销"))
        self.pushButton.setText(_translate("MainWindow", "保存"))
        self.labellist.setTabText(self.labellist.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.labellist.setTabText(self.labellist.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

