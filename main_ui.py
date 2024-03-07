# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("#MainWindow {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 13pt;\n"
"    border: 2px solid #ddd;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: black;\n"
"   min-width: 120px;\n"
"}\n"
"QPushButton#btnAdd {\n"
"    color: #fff;\n"
"    background-color: #0d6efd;\n"
"}\n"
"QPushButton#btnAdd:hover {\n"
"    background-color: #0055ff;\n"
"}\n"
"QPushButton#btnAdd:pressed {\n"
"    border-color: #98c1fe;\n"
"}\n"
"QPushButton#btnEdit {\n"
"    color: #fff;\n"
"    background-color: purple;\n"
"}\n"
"QPushButton#btnEdit:hover {\n"
"    background-color: rgb(210, 6, 210);\n"
"}\n"
"QPushButton#btnEdit:pressed {\n"
"    border-color: rgb(250, 159, 250);\n"
"}\n"
"QPushButton#btnRemove {\n"
"    color: #fff;\n"
"    background-color: #198754;\n"
"}\n"
"QPushButton#btnRemove:hover {\n"
"    background-color: #157347;\n"
"}\n"
"QPushButton#btnRemove:pressed {\n"
"    border-color: #9dccb6;\n"
"}\n"
"QPushButton#btnClear {\n"
"    color: #fff;\n"
"    background-color: #dc3545;\n"
"}\n"
"QPushButton#btnClear:hover {\n"
"    background-color: #bb2d3b;\n"
"}\n"
"QPushButton#btnClear:pressed {\n"
"    border-color: #f0a9b0;\n"
"}\n"
"QListWidget {\n"
"    color: #000;\n"
"    font-size: 13pt;\n"
"}\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"}\n"
"QListWidget::item:selected {\n"
"   color: #000;\n"
"    background-color: rgb(162, 246, 192);\n"
"}\n"
"QCheckBox {\n"
"font-size: 13pt;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 0;\n"
"    background-color: #fff;\n"
"    width: 5px;\n"
"    margin: 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #aa00ff;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background-color: #aa00ff;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: #aa00ff;\n"
"    height: 0px;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listActor = QtWidgets.QListWidget(self.centralwidget)
        self.listActor.setObjectName("listActor")
        self.horizontalLayout.addWidget(self.listActor)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setObjectName("btnEdit")
        self.verticalLayout.addWidget(self.btnEdit)
        self.btnRemove = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout.addWidget(self.btnRemove)
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout.addWidget(self.btnClear)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnRemove.setText(_translate("MainWindow", "Remove"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
