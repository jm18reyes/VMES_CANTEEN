# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteItem_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteMenu(object):
    def setupUi(self, deleteMenu):
        deleteMenu.setObjectName("deleteMenu")
        deleteMenu.resize(510, 410)
        self.centralwidget = QtWidgets.QWidget(deleteMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.dltMenu_bfastBtn = QtWidgets.QPushButton(self.centralwidget)
        self.dltMenu_bfastBtn.setGeometry(QtCore.QRect(20, 30, 151, 61))
        self.dltMenu_bfastBtn.setObjectName("dltMenu_bfastBtn")
        self.dltMenu_lunchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.dltMenu_lunchBtn.setGeometry(QtCore.QRect(180, 30, 151, 61))
        self.dltMenu_lunchBtn.setObjectName("dltMenu_lunchBtn")
        self.dltMenu_snackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.dltMenu_snackBtn.setGeometry(QtCore.QRect(340, 30, 151, 61))
        self.dltMenu_snackBtn.setObjectName("dltMenu_snackBtn")
        self.dltMenu_menuCombo = QtWidgets.QComboBox(self.centralwidget)
        self.dltMenu_menuCombo.setGeometry(QtCore.QRect(20, 110, 471, 41))
        self.dltMenu_menuCombo.setObjectName("dltMenu_menuCombo")
        self.remove_item = QtWidgets.QPushButton(self.centralwidget)
        self.remove_item.setGeometry(QtCore.QRect(190, 300, 131, 51))
        self.remove_item.setObjectName("remove_item")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.food_lbl = QtWidgets.QLabel(self.centralwidget)
        self.food_lbl.setGeometry(QtCore.QRect(140, 230, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.food_lbl.setFont(font)
        self.food_lbl.setObjectName("food_lbl")
        deleteMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(deleteMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        deleteMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(deleteMenu)
        self.statusbar.setObjectName("statusbar")
        deleteMenu.setStatusBar(self.statusbar)

        self.retranslateUi(deleteMenu)
        QtCore.QMetaObject.connectSlotsByName(deleteMenu)

    def retranslateUi(self, deleteMenu):
        _translate = QtCore.QCoreApplication.translate
        deleteMenu.setWindowTitle(_translate("deleteMenu", "Delete Menu Item"))
        self.dltMenu_bfastBtn.setText(_translate("deleteMenu", "Breakfast"))
        self.dltMenu_lunchBtn.setText(_translate("deleteMenu", "Lunch"))
        self.dltMenu_snackBtn.setText(_translate("deleteMenu", "Snack"))
        self.remove_item.setText(_translate("deleteMenu", "REMOVE ITEM"))
        self.label_4.setText(_translate("deleteMenu", "FOOD:"))
        self.food_lbl.setText(_translate("deleteMenu", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteMenu = QtWidgets.QMainWindow()
    ui = Ui_deleteMenu()
    ui.setupUi(deleteMenu)
    deleteMenu.show()
    sys.exit(app.exec_())
