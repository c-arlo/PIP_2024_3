import sys

import numpy
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E5_IMC.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E5 - Calcular IMC de una persona")
        # Área de los Signals
        try:
            self.btn_calc.clicked.connect(self.calcular)
        except Exception as e:
            print(e)

        try:
            self.cb_peso.currentIndexChanged.connect(self.cambiarAltura)
        except Exception as e:
            print(e)

        try:
            self.cb_altura.currentIndexChanged.connect(self.cambiarPeso)
        except Exception as e:
            print(e)

    # Área de los Slots
    def calcular(self):
        peso = float(self.txt_peso.text())
        altura = float(self.txt_altura.text())
        imc = peso / (altura ** 2)
        if self.cb_peso.currentIndex() == 1:
            imc *= 703
        self.txt_imc.setText(str(round(imc, 1)))

    def cambiarAltura(self):
        self.cb_altura.setCurrentIndex(self.cb_peso.currentIndex())

    def cambiarPeso(self):
        self.cb_peso.setCurrentIndex(self.cb_altura.currentIndex())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
