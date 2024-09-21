import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P17_SliderNombres_Correcto.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lista_nombres = [
            "Angel S.", "Jazmin", "Carolina", "Fernando", "Dilan", "Maciel", "Yahir", "Carlos", "Angel A."
        ]
        self.index_nombre = 0
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])
        self.txt_nombre.setEnabled(False)
        self.btn_control.clicked.connect(self.control)

        self.hiloSegundoPlano = QtCore.QTimer()
        self.hiloSegundoPlano.timeout.connect(self.contar)

    def control(self):
        texto_boton = self.btn_control.text()
        if texto_boton == "INICIAR":
            self.index_nombre = 0
            self.hiloSegundoPlano.start(100) #inicia el hilo en segundo plano
            self.btn_control.setText("DETENER")
        else:
            self.hiloSegundoPlano.stop()
            self.btn_control.setText("INICIAR")

    def contar(self):
        self.index_nombre += 1
        self.index_nombre %= len(self.lista_nombres)
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

