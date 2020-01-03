# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminPage(object):
    def setupUi(self, adminPage):
        adminPage.setObjectName("adminPage")
        adminPage.resize(396, 450)
        self.centralwidget = QtWidgets.QWidget(adminPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.user_reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.user_reg_btn.setGeometry(QtCore.QRect(40, 250, 321, 41))
        self.user_reg_btn.setObjectName("user_reg_btn")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(40, 350, 321, 41))
        self.logout_btn.setObjectName("logout_btn")
        self.hmpg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hmpg_btn.setGeometry(QtCore.QRect(40, 100, 321, 41))
        self.hmpg_btn.setObjectName("hmpg_btn")
        self.acc_mngBtn = QtWidgets.QPushButton(self.centralwidget)
        self.acc_mngBtn.setGeometry(QtCore.QRect(40, 300, 321, 41))
        self.acc_mngBtn.setObjectName("acc_mngBtn")
        self.menu_mngBtn = QtWidgets.QPushButton(self.centralwidget)
        self.menu_mngBtn.setGeometry(QtCore.QRect(40, 150, 321, 41))
        self.menu_mngBtn.setObjectName("menu_mngBtn")
        self.totalEarn_btn = QtWidgets.QPushButton(self.centralwidget)
        self.totalEarn_btn.setGeometry(QtCore.QRect(40, 200, 321, 41))
        self.totalEarn_btn.setObjectName("totalEarn_btn")
        adminPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 26))
        self.menubar.setObjectName("menubar")
        adminPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminPage)
        self.statusbar.setObjectName("statusbar")
        adminPage.setStatusBar(self.statusbar)

        self.retranslateUi(adminPage)
        QtCore.QMetaObject.connectSlotsByName(adminPage)

    def retranslateUi(self, adminPage):
        _translate = QtCore.QCoreApplication.translate
        adminPage.setWindowTitle(_translate("adminPage", "ADMIN PAGE"))
        self.label.setText(_translate("adminPage", "VMES CANTEEN"))
        self.user_reg_btn.setText(_translate("adminPage", "USER REGISTRATION"))
        self.logout_btn.setText(_translate("adminPage", "LOGOUT"))
        self.hmpg_btn.setText(_translate("adminPage", "HOMEPAGE"))
        self.acc_mngBtn.setText(_translate("adminPage", "ACCOUNT MANAGEMENT"))
        self.menu_mngBtn.setText(_translate("adminPage", "MENU MANAGEMENT"))
        self.totalEarn_btn.setText(_translate("adminPage", "TOTAL EARNINGS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminPage = QtWidgets.QMainWindow()
    ui = Ui_adminPage()
    ui.setupUi(adminPage)
    adminPage.show()
    sys.exit(app.exec_())
