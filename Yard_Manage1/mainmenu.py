# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#teset edit sdf


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.QC_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.QC_pushButton.setMinimumSize(QtCore.QSize(200, 60))
        self.QC_pushButton.setObjectName("QC_pushButton")
        self.gridLayout.addWidget(self.QC_pushButton, 0, 0, 1, 1)
        self.QA_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.QA_pushButton.setMinimumSize(QtCore.QSize(200, 60))
        self.QA_pushButton.setObjectName("QA_pushButton")
        self.gridLayout.addWidget(self.QA_pushButton, 1, 0, 1, 1)
        self.Stats_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Stats_pushButton.setMinimumSize(QtCore.QSize(200, 60))
        self.Stats_pushButton.setObjectName("Stats_pushButton")
        self.gridLayout.addWidget(self.Stats_pushButton, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #testing edit save sdff


        class MainWindow(QtWidgets.QMainWindow):

            def__init__(self):
                super(MainWindow, self).__init__()

                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QC_pushButton.setText(_translate("MainWindow", "Quality Control"))
        self.QA_pushButton.setText(_translate("MainWindow", "Quality Assurance"))
        self.Stats_pushButton.setText(_translate("MainWindow", "Statistics"))
