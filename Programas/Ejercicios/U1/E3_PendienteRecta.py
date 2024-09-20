import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E3_PendienteRecta.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("E3 - Obtener la pendiente de una recta")
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
        m = (y2-y1)/(x2-x1)
        self.txt_res.setText(str(round(m,2)))
        print(m)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())