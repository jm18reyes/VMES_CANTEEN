# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderedItems_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_orderedItems(object):
    def setupUi(self, orderedItems):
        orderedItems.setObjectName("orderedItems")
        orderedItems.resize(503, 577)
        self.centralwidget = QtWidgets.QWidget(orderedItems)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.total_lbl = QtWidgets.QLabel(self.centralwidget)
        self.total_lbl.setGeometry(QtCore.QRect(160, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.total_lbl.setFont(font)
        self.total_lbl.setObjectName("total_lbl")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 481, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(380, 30, 111, 41))
        self.del_btn.setObjectName("del_btn")
        orderedItems.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(orderedItems)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 26))
        self.menubar.setObjectName("menubar")
        orderedItems.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(orderedItems)
        self.statusbar.setObjectName("statusbar")
        orderedItems.setStatusBar(self.statusbar)

        self.retranslateUi(orderedItems)
        QtCore.QMetaObject.connectSlotsByName(orderedItems)

    def retranslateUi(self, orderedItems):
        _translate = QtCore.QCoreApplication.translate
        orderedItems.setWindowTitle(_translate("orderedItems", "Sold Items"))
        self.label.setText(_translate("orderedItems", "TOTAL: P"))
        self.total_lbl.setText(_translate("orderedItems", "0.00"))
        self.label_2.setText(_translate("orderedItems", "DATE"))
        self.label_3.setText(_translate("orderedItems", "PRICE"))
        self.label_4.setText(_translate("orderedItems", "ITEM"))
        self.del_btn.setText(_translate("orderedItems", "DELETE ALL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    orderedItems = QtWidgets.QMainWindow()
    ui = Ui_orderedItems()
    ui.setupUi(orderedItems)
    orderedItems.show()
    sys.exit(app.exec_())
