# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Quality_failure_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 321)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.vessel_label = QtWidgets.QLabel(Dialog)
        self.vessel_label.setObjectName("vessel_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vessel_label)
        self.vessel_comboBox = QtWidgets.QComboBox(Dialog)
        self.vessel_comboBox.setEditable(True)
        self.vessel_comboBox.setObjectName("vessel_comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vessel_comboBox)
        self.SOC_Label = QtWidgets.QLabel(Dialog)
        self.SOC_Label.setObjectName("SOC_Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SOC_Label)
        self.SOC_comboBox = QtWidgets.QComboBox(Dialog)
        self.SOC_comboBox.setEditable(True)
        self.SOC_comboBox.setObjectName("SOC_comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SOC_comboBox)
        self.Defect_Label = QtWidgets.QLabel(Dialog)
        self.Defect_Label.setObjectName("Defect_Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Defect_Label)
        self.defecttype_comboBox = QtWidgets.QComboBox(Dialog)
        self.defecttype_comboBox.setEditable(True)
        self.defecttype_comboBox.setObjectName("defecttype_comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.defecttype_comboBox)
        self.Weldtype_labe = QtWidgets.QLabel(Dialog)
        self.Weldtype_labe.setObjectName("Weldtype_labe")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Weldtype_labe)
        self.wledtype_comboBox = QtWidgets.QComboBox(Dialog)
        self.wledtype_comboBox.setEditable(True)
        self.wledtype_comboBox.setObjectName("wledtype_comboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wledtype_comboBox)
        self.location_label = QtWidgets.QLabel(Dialog)
        self.location_label.setObjectName("location_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.location_label)
        self.location_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.location_lineEdit.setObjectName("location_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.location_lineEdit)
        self.date_label = QtWidgets.QLabel(Dialog)
        self.date_label.setObjectName("date_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.date_label)
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.save_pushButton = QtWidgets.QPushButton(Dialog)
        self.save_pushButton.setObjectName("save_pushButton")
        self.gridLayout.addWidget(self.save_pushButton, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.vessel_label.setText(_translate("Dialog", "Vessel/Project:"))
        self.SOC_Label.setText(_translate("Dialog", "Stage of Construction:"))
        self.Defect_Label.setText(_translate("Dialog", "Defect Type:"))
        self.Weldtype_labe.setText(_translate("Dialog", "Weld Type:"))
        self.location_label.setText(_translate("Dialog", "Location:"))
        self.date_label.setText(_translate("Dialog", "Date:"))
        self.save_pushButton.setText(_translate("Dialog", "Save"))
        self.label.setText(_translate("Dialog", "Edit Quality Failue Entry"))
