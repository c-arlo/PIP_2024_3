import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E7_Pitagoras.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E7 - Teorema de pitagoras")
        # Área de los Signals
        try:
            self.btn_calc.clicked.connect(self.calcular)
        except Exception as e:
            print(e)

    # Área de los Slots
    def calcular(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        c = a**2 + b**2
        self.txt_res.setText(str(round(c,2)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())