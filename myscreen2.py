# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myscreen2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transportista = QtWidgets.QLineEdit(self.centralwidget)
        self.transportista.setGeometry(QtCore.QRect(10, 80, 311, 23))
        self.transportista.setObjectName("transportista")
        self.numCosto = QtWidgets.QLineEdit(self.centralwidget)
        self.numCosto.setGeometry(QtCore.QRect(210, 120, 113, 23))
        self.numCosto.setText("")
        self.numCosto.setObjectName("numCosto")
        self.guardar = QtWidgets.QPushButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(70, 210, 211, 21))
        self.guardar.setObjectName("guardar")
        self.actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.actualizar.setGeometry(QtCore.QRect(70, 262, 211, 21))
        self.actualizar.setObjectName("actualizar")
        self.listaFletes = QtWidgets.QTableWidget(self.centralwidget)
        self.listaFletes.setGeometry(QtCore.QRect(370, 70, 256, 192))
        self.listaFletes.setObjectName("listaFletes")
        self.listaFletes.setColumnCount(0)
        self.listaFletes.setRowCount(0)
        self.label_nombreTrans = QtWidgets.QLabel(self.centralwidget)
        self.label_nombreTrans.setGeometry(QtCore.QRect(10, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_nombreTrans.setFont(font)
        self.label_nombreTrans.setObjectName("label_nombreTrans")
        self.label_costoFlete = QtWidgets.QLabel(self.centralwidget)
        self.label_costoFlete.setGeometry(QtCore.QRect(110, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_costoFlete.setFont(font)
        self.label_costoFlete.setObjectName("label_costoFlete")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.actualizar.setText(_translate("MainWindow", "Actualizar"))
        self.label_nombreTrans.setText(_translate("MainWindow", "Transportista"))
        self.label_costoFlete.setText(_translate("MainWindow", "Costo Flete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
