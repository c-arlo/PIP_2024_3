import sys
from PyQt5 import uic, QtWidgets
import P3_Calcula_IMC as interfaz

#qtCreatorFile = "P0_Plantilla.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btnSumar.clicked.connect(self.calcularIMC)

    # Área de los Slots
    def calcularIMC(self):
        a = float(self.txtAltura.text())
        p = float(self.txtPeso.text())
        r = p / a**2
        r = round(r, 2)
        self.mensaje("IMC = "+str(r))

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())