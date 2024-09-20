import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P3_IntroEntradaSalidaTexto.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("P3_IntroEntradaSalida")

        # Área de los Signals (Eventos)
        try:
            self.btn_saludar.clicked.connect(self.saludar)
        except Exception as e:
            print(e)


    # Área de los Slots (Funciones)
    def saludar(self):
        cadena = "Hola usuario el cual su nombre es... "
        nombre = self.txt_nombre.text()
        if len(nombre)==0:
            cadena += " al parecer nada...."
        if len(nombre)<=1 and len(nombre)!=0:
            cadena += nombre + "... como si eso fuera posible..."
        else:
            cadena += nombre
        self.mensaje(cadena)

    def mensaje(self,texto):
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Mensaje")
        m.setText(texto)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())