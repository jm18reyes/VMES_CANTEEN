from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidget,QTableWidgetItem
import sys
from functools import partial

sys.path.insert(0, '../DAL')
from handler import DataHandler
dh = DataHandler('../VMES.db')

sys.path.insert(0, '../UI')
import orderedItems_ui

class Main(QtWidgets.QMainWindow, orderedItems_ui.Ui_orderedItems):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.del_btn.clicked.connect(self.deleteAll)
        self.priceMap = {}
        self.dateMap = {}
        self.total = 0
        self.food = ""
        self.price = 0
        self.date = ""
        self.f = []
        self.p = []
        self.d = []
        self.newD = []
        self.results = dh.getAllOrders()

        for x in self.results:
            self.priceMap[x[0]] = x[1]
            self.dateMap[x[0]] = x[2]
            self.f.append(x[0])
            self.p.append(x[1])
            self.total = self.total + x[1]


        self.total_lbl.setText(str(self.total))
        print(self.priceMap)
        print(self.dateMap)

        for y in self.f:
            dT = self.dateMap[y]
            dT = list(dT)
            del dT[10:]
            dT = ''.join(map(str,dT))
            print(dT)
            self.dateMap[y] = str(dT)
            self.d.append(str(dT))

        self.tableWidget.setRowCount(len(self.f))
        self.tableWidget.setColumnCount(3)

        m = 0
        for a in self.d:
            self.tableWidget.setItem(m,0, QTableWidgetItem(a))

            m += 1
        m = 0
        for b in self.f:
            self.tableWidget.setItem(m,1, QTableWidgetItem(b))
            m += 1


        print(self.p)
        m = 0
        for c in self.p:
            print(c)
            self.tableWidget.setItem(m,2, QTableWidgetItem(str(c)))
            m += 1

    def deleteAll(self):
        dh.deleteSoldItems()
        self.msg = QMessageBox()
        self.msg.setWindowTitle("SUCCESS")
        self.msg.setText("Items Successfully Cleared")
        x = self.msg.exec()
        self.end()
        self.win2 = Main()
        self.win2.show()

    def end(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())