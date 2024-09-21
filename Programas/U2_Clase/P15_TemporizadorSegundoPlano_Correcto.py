import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P15_TemporizadorSegundoPlano_Correcto.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lcdNumber.setNumDigits(4)
        self.valor_inicial = 10
        self.lcdNumber.display(self.valor_inicial)
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.hiloSegundoPlano = QtCore.QTimer()
        self.hiloSegundoPlano.timeout.connect(self.contar)

    def iniciar(self):
        self.valor_inicial = 10
        self.hiloSegundoPlano.start(250) #inicia el hilo en segundo plano
        # con un temporizador de 10 por defecto

    def contar(self):
        print(self.valor_inicial)
        self.lcdNumber.display(self.valor_inicial)
        self.valor_inicial -= 1
        if self.valor_inicial == -1:
            self.hiloSegundoPlano.stop()


    # Área de los Slots
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

