import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E8_CalculoDiscriminante.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E8 - Calculo de la discriminante")
        # Área de los Signals
        try:
            self.btn_calc.clicked.connect(self.calcular)
        except Exception as e:
            print(e)

    # Área de los Slots
    def calcular(self):
        a = float(self.txt_a.text())
        b = float(self.txt_b.text())
        c = float(self.txt_c.text())
        disc = b**2 - 4*a*c
        self.txt_res.setText(str(round(disc,2)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())