import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P16_SliderNombres.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lista_nombres = [
            "Pedro", "Juan", "Paola", "Maria", "Jesus", "Marcy"
        ]
        self.index_nombre = 0
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])
        self.txt_nombre.setEnabled(False)
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.hiloSegundoPlano = QtCore.QTimer()
        self.hiloSegundoPlano.timeout.connect(self.contar)

    def iniciar(self):
        self.index_nombre = 0
        self.hiloSegundoPlano.start(500) #inicia el hilo en segundo plano
        # con un temporizador de 10 por defecto

    def contar(self):
        self.index_nombre += 1
        self.index_nombre %= len(self.lista_nombres)
        self.txt_nombre.setText(self.lista_nombres[self.index_nombre])


    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

