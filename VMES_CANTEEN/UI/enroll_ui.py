# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enroll.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userRegistration(object):
    def setupUi(self, userRegistration):
        userRegistration.setObjectName("userRegistration")
        userRegistration.resize(800, 570)
        self.centralwidget = QtWidgets.QWidget(userRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.job_combo = QtWidgets.QComboBox(self.centralwidget)
        self.job_combo.setGeometry(QtCore.QRect(320, 360, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.job_combo.setFont(font)
        self.job_combo.setObjectName("job_combo")
        self.job_combo.addItem("")
        self.job_combo.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 360, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.username_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.username_reg.setGeometry(QtCore.QRect(320, 80, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username_reg.setFont(font)
        self.username_reg.setObjectName("username_reg")
        self.pass_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_reg.setGeometry(QtCore.QRect(320, 170, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pass_reg.setFont(font)
        self.pass_reg.setObjectName("pass_reg")
        self.pass2_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.pass2_reg.setGeometry(QtCore.QRect(320, 270, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pass2_reg.setFont(font)
        self.pass2_reg.setObjectName("pass2_reg")
        self.save_reg = QtWidgets.QPushButton(self.centralwidget)
        self.save_reg.setGeometry(QtCore.QRect(320, 460, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save_reg.setFont(font)
        self.save_reg.setObjectName("save_reg")
        userRegistration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(userRegistration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        userRegistration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(userRegistration)
        self.statusbar.setObjectName("statusbar")
        userRegistration.setStatusBar(self.statusbar)

        self.retranslateUi(userRegistration)
        QtCore.QMetaObject.connectSlotsByName(userRegistration)

    def retranslateUi(self, userRegistration):
        _translate = QtCore.QCoreApplication.translate
        userRegistration.setWindowTitle(_translate("userRegistration", "USER REGISTRATION"))
        self.label.setText(_translate("userRegistration", "USERNAME:"))
        self.label_2.setText(_translate("userRegistration", "PASSWORD:"))
        self.label_3.setText(_translate("userRegistration", "RETYPE PASSWORD:"))
        self.job_combo.setItemText(0, _translate("userRegistration", "admin"))
        self.job_combo.setItemText(1, _translate("userRegistration", "regular"))
        self.label_4.setText(_translate("userRegistration", "ACCOUNT TYPE:"))
        self.save_reg.setText(_translate("userRegistration", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userRegistration = QtWidgets.QMainWindow()
    ui = Ui_userRegistration()
    ui.setupUi(userRegistration)
    userRegistration.show()
    sys.exit(app.exec_())
