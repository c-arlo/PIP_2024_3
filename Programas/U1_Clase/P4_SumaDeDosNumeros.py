import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P4_SumaDeDosNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("P4_SumaDeDosNumeros")

        # Área de los Signals (Eventos)
        try:
            self.btn_sumar.clicked.connect(self.sumar)
        except Exception as e:
            print(e)


    # Área de los Slots (Funciones)
    def sumar(self):
        n1 = self.txt_numero1.text() #str
        n2 = self.txt_numero2.text() #str
        n1 = int(n1)
        n2 = int(n2)
        r = n1 + n2
        cadena = "El resultado de la suma es = " + str(r)
        self.mensaje(cadena)

    def mensaje(self,texto):
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Resultado")
        m.setText(texto)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())