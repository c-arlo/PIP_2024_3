import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E4_PerimPoligReg.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E4 - Calcular perimetro de un poligono regular")
        # Área de los Signals
        try:
            self.btn_calc.clicked.connect(self.calcular)
        except Exception as e:
            print(e)

        try:
            self.cb_medida.currentTextChanged.connect(self.cambiarMedida)
        except Exception as e:
            print(e)


    # Área de los Slots
    def calcular(self):
        n = int(self.txt_lados.text())
        s = int(self.txt_long.text())
        P = n*s
        self.txt_res.setText(str(round(P,2)))
        print(P)

    def cambiarMedida(self):
        self.lbl_medida.setText(self.cb_medida.currentText()) #print(self.cb_medida.currentText())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())