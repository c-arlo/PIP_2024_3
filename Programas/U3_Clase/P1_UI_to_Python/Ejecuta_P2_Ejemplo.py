import sys
from PyQt5 import uic, QtWidgets
import P2_Ejemplo as interfaz

#qtCreatorFile = "P0_Plantilla.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btnSumar.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        a = int(self.txtNum1.text())
        b = int(self.txtNum2.text())
        c = int(self.txtNum3.text())
        r = a + b + c
        self.mensaje("Resultado = "+str(r))

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())