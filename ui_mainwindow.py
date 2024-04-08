# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui-main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(848, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 831, 22))
        self.lineEdit.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 71, 16))
        self.label.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 71, 16))
        self.label_2.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 70, 831, 22))
        self.lineEdit_2.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 120, 831, 22))
        self.comboBox.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid #ffffff;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 81, 16))
        self.label_3.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 150, 831, 24))
        self.pushButton.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid #ffffff;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 180, 831, 24))
        self.pushButton_2.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid #ffffff;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 210, 831, 24))
        self.pushButton_3.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid #ffffff;")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 290, 831, 301))
        self.tableView.setTabletTracking(False)
        self.tableView.setStyleSheet(u"color: black;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid #ffffff;")
        self.tableView.setShowGrid(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 240, 151, 41))
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 240, 131, 41))
        self.label_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 240, 121, 41))
        self.label_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(580, 240, 131, 41))
        self.label_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(690, 240, 131, 41))
        self.label_8.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(730, 240, 121, 41))
        self.label_9.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0440\u043e\u043d\u0430 A:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0440\u043e\u043d\u0430 B:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1x1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"3x5", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"5x5", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"7x7", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5x10", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0456\u0440 \u0444\u0456\u0433\u0443\u0440\u0438:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0430\u0445\u0443\u0432\u0430\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0434\u043e \u0442\u0430\u0431\u043b\u0438\u0446\u0456", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0440\u043e\u043d\u0430 A", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0440\u043e\u043d\u0430 B", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u043d\u0430 \u0444\u0456\u0433\u0443\u0440\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0449\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0444\u0456\u0433\u0443\u0440", None))
    # retranslateUi

