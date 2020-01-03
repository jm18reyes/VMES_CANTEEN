# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuManagement.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menuManagement(object):
    def setupUi(self, menuManagement):
        menuManagement.setObjectName("menuManagement")
        menuManagement.resize(456, 370)
        self.centralwidget = QtWidgets.QWidget(menuManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.add_menu = QtWidgets.QPushButton(self.centralwidget)
        self.add_menu.setGeometry(QtCore.QRect(100, 60, 261, 51))
        self.add_menu.setObjectName("add_menu")
        self.change_price = QtWidgets.QPushButton(self.centralwidget)
        self.change_price.setGeometry(QtCore.QRect(100, 140, 261, 51))
        self.change_price.setObjectName("change_price")
        self.delete_menu = QtWidgets.QPushButton(self.centralwidget)
        self.delete_menu.setGeometry(QtCore.QRect(100, 220, 261, 51))
        self.delete_menu.setObjectName("delete_menu")
        menuManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menuManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 26))
        self.menubar.setObjectName("menubar")
        menuManagement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menuManagement)
        self.statusbar.setObjectName("statusbar")
        menuManagement.setStatusBar(self.statusbar)

        self.retranslateUi(menuManagement)
        QtCore.QMetaObject.connectSlotsByName(menuManagement)

    def retranslateUi(self, menuManagement):
        _translate = QtCore.QCoreApplication.translate
        menuManagement.setWindowTitle(_translate("menuManagement", "Manage Menu"))
        self.add_menu.setText(_translate("menuManagement", "Add Menu Item"))
        self.change_price.setText(_translate("menuManagement", "Change Price"))
        self.delete_menu.setText(_translate("menuManagement", "Delete Menu Item"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuManagement = QtWidgets.QMainWindow()
    ui = Ui_menuManagement()
    ui.setupUi(menuManagement)
    menuManagement.show()
    sys.exit(app.exec_())
