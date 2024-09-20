import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E9_ParImpar.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E9 - Determinar si un numero es par o impar")
        # Área de los Signals

        self.btn_calc.clicked.connect(self.calcular)


    # Área de los Slots
    def calcular(self):
        n = int(self.txt_num.text())
        if (n%2) != 0:
            self.txt_res.setText("Impar")
        else:
            self.txt_res.setText("Par")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())