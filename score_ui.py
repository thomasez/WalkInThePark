# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created: Sun Aug  4 12:15:34 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 527)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Next = QtGui.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(470, 70, 122, 77))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.Next.setFont(font)
        self.Next.setObjectName("Next")
        self.Plus = QtGui.QPushButton(self.centralwidget)
        self.Plus.setGeometry(QtCore.QRect(470, 150, 122, 77))
        font = QtGui.QFont()
        font.setPointSize(42)
        self.Plus.setFont(font)
        self.Plus.setObjectName("Plus")
        self.Minus = QtGui.QPushButton(self.centralwidget)
        self.Minus.setGeometry(QtCore.QRect(260, 150, 122, 77))
        font = QtGui.QFont()
        font.setPointSize(42)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Minus.setFont(font)
        self.Minus.setObjectName("Minus")
        self.Throws = QtGui.QLCDNumber(self.centralwidget)
        self.Throws.setGeometry(QtCore.QRect(390, 150, 77, 77))
        self.Throws.setNumDigits(2)
        self.Throws.setObjectName("Throws")
        self.Basketnum = QtGui.QLabel(self.centralwidget)
        self.Basketnum.setGeometry(QtCore.QRect(10, 10, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.Basketnum.setFont(font)
        self.Basketnum.setObjectName("Basketnum")
        self.Previous = QtGui.QPushButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(260, 70, 122, 77))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.Previous.setFont(font)
        self.Previous.setObjectName("Previous")
        self.Done = QtGui.QPushButton(self.centralwidget)
        self.Done.setEnabled(True)
        self.Done.setGeometry(QtCore.QRect(470, 340, 122, 77))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.Done.setFont(font)
        self.Done.setObjectName("Done")
        self.Playername = QtGui.QLabel(self.centralwidget)
        self.Playername.setGeometry(QtCore.QRect(10, 170, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Playername.setFont(font)
        self.Playername.setObjectName("Playername")
        self.Total = QtGui.QLabel(self.centralwidget)
        self.Total.setGeometry(QtCore.QRect(10, 340, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.Total.setFont(font)
        self.Total.setObjectName("Total")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 36))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuGolf = QtGui.QMenu(self.menubar)
        self.menuGolf.setObjectName("menuGolf")
        self.menuPebble = QtGui.QMenu(self.menubar)
        self.menuPebble.setObjectName("menuPebble")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose_course = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionChoose_course.setFont(font)
        self.actionChoose_course.setObjectName("actionChoose_course")
        self.actionSave_course = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionSave_course.setFont(font)
        self.actionSave_course.setObjectName("actionSave_course")
        self.actionNew_course = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionNew_course.setFont(font)
        self.actionNew_course.setObjectName("actionNew_course")
        self.actionOpen_score = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionOpen_score.setFont(font)
        self.actionOpen_score.setObjectName("actionOpen_score")
        self.actionNew_Score = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionNew_Score.setFont(font)
        self.actionNew_Score.setObjectName("actionNew_Score")
        self.actionAbout = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClose = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionClose.setFont(font)
        self.actionClose.setObjectName("actionClose")
        self.actionConnect = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionConnect.setFont(font)
        self.actionConnect.setObjectName("actionConnect")
        self.actionPair = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionPair.setFont(font)
        self.actionPair.setObjectName("actionPair")
        self.actionDisconnect = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.actionDisconnect.setFont(font)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.menuGolf.addAction(self.actionChoose_course)
        self.menuGolf.addAction(self.actionSave_course)
        self.menuGolf.addAction(self.actionNew_course)
        self.menuGolf.addAction(self.actionOpen_score)
        self.menuGolf.addAction(self.actionNew_Score)
        self.menuGolf.addAction(self.actionAbout)
        self.menuGolf.addAction(self.actionClose)
        self.menubar.addAction(self.menuGolf.menuAction())
        self.menuPebble.addAction(self.actionConnect)
        self.menuPebble.addAction(self.actionPair)
        self.menuPebble.addAction(self.actionDisconnect)
        self.menubar.addAction(self.menuPebble.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Disc Golf Scorecard", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "Foo", None, QtGui.QApplication.UnicodeUTF8))
        self.Next.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.Plus.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.Minus.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.Basketnum.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.Previous.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.Done.setText(QtGui.QApplication.translate("MainWindow", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.Playername.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.Total.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGolf.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPebble.setTitle(QtGui.QApplication.translate("MainWindow", "Pebble", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChoose_course.setText(QtGui.QApplication.translate("MainWindow", "Choose Course", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_course.setText(QtGui.QApplication.translate("MainWindow", "Save Walk As Score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_course.setText(QtGui.QApplication.translate("MainWindow", "New course", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_score.setText(QtGui.QApplication.translate("MainWindow", "Open score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Score.setText(QtGui.QApplication.translate("MainWindow", "New Score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPair.setText(QtGui.QApplication.translate("MainWindow", "Pair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))

