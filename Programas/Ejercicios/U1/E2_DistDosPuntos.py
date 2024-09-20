import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E2_DistDosPuntos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E2 - Obtener la distancia entre dos puntos")
        # Área de los Signals
        try:
            self.btn_calc.clicked.connect(self.calcular)
        except Exception as e:
            print(e)

    # Área de los Slots
    def calcular(self):
        x1 = int(self.txt_x1.text())
        y1 = int(self.txt_y1.text())
        x2 = int(self.txt_x2.text())
        y2 = int(self.txt_y2.text())
        d = numpy.sqrt((x2-x1)**2 + (y2-y1)**2)
        self.txt_res.setText(str(round(d,2)))
        print(d)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())