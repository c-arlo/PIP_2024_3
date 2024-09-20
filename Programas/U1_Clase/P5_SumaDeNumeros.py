import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P5_SumaDeNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("P5_SumaDeNumeros")

        # Área de los Signals (Eventos)
        try:
            self.btn_sumar.clicked.connect(self.sumar)
        except Exception as e:
            print(e)


    # Área de los Slots (Funciones)
    def sumar(self):
        n = self.txt_numeros.text() #str
        r = eval(n)
        self.txt_resultado.setText(str(r))
        #self.mensaje("El resultado de la suma es:" + str(r))

    """
    def mensaje(self,texto):
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Resultado")
        m.setText(texto)
        m.exec()
    """

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())