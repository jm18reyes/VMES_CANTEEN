# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addMenu_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addMenuItem(object):
    def setupUi(self, addMenuItem):
        addMenuItem.setObjectName("addMenuItem")
        addMenuItem.resize(615, 507)
        font = QtGui.QFont()
        font.setPointSize(14)
        addMenuItem.setFont(font)
        self.centralwidget = QtWidgets.QWidget(addMenuItem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.addMenu_mealCombo = QtWidgets.QComboBox(self.centralwidget)
        self.addMenu_mealCombo.setGeometry(QtCore.QRect(150, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addMenu_mealCombo.setFont(font)
        self.addMenu_mealCombo.setObjectName("addMenu_mealCombo")
        self.addMenu_mealCombo.addItem("")
        self.addMenu_mealCombo.addItem("")
        self.addMenu_mealCombo.addItem("")
        self.chosen_meal = QtWidgets.QLabel(self.centralwidget)
        self.chosen_meal.setGeometry(QtCore.QRect(230, 100, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chosen_meal.setFont(font)
        self.chosen_meal.setObjectName("chosen_meal")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.new_menuItem = QtWidgets.QLineEdit(self.centralwidget)
        self.new_menuItem.setGeometry(QtCore.QRect(10, 220, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_menuItem.setFont(font)
        self.new_menuItem.setObjectName("new_menuItem")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.add_price = QtWidgets.QLineEdit(self.centralwidget)
        self.add_price.setGeometry(QtCore.QRect(110, 300, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_price.setFont(font)
        self.add_price.setObjectName("add_price")
        self.save_menuItem = QtWidgets.QPushButton(self.centralwidget)
        self.save_menuItem.setGeometry(QtCore.QRect(240, 380, 131, 51))
        self.save_menuItem.setObjectName("save_menuItem")
        addMenuItem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addMenuItem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 26))
        self.menubar.setObjectName("menubar")
        addMenuItem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addMenuItem)
        self.statusbar.setObjectName("statusbar")
        addMenuItem.setStatusBar(self.statusbar)

        self.retranslateUi(addMenuItem)
        QtCore.QMetaObject.connectSlotsByName(addMenuItem)

    def retranslateUi(self, addMenuItem):
        _translate = QtCore.QCoreApplication.translate
        addMenuItem.setWindowTitle(_translate("addMenuItem", "Add Menu Item"))
        self.label.setText(_translate("addMenuItem", "Meal Time:"))
        self.addMenu_mealCombo.setItemText(0, _translate("addMenuItem", "breakfast"))
        self.addMenu_mealCombo.setItemText(1, _translate("addMenuItem", "lunch"))
        self.addMenu_mealCombo.setItemText(2, _translate("addMenuItem", "snack"))
        self.chosen_meal.setText(_translate("addMenuItem", "Breakfast"))
        self.label_3.setText(_translate("addMenuItem", "Enter New Item Below"))
        self.label_4.setText(_translate("addMenuItem", "Price: P"))
        self.save_menuItem.setText(_translate("addMenuItem", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addMenuItem = QtWidgets.QMainWindow()
    ui = Ui_addMenuItem()
    ui.setupUi(addMenuItem)
    addMenuItem.show()
    sys.exit(app.exec_())
