import random
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E11_Ahorcado.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.listPalabras = ["fresco", "mensaje", "ventana", "ahorcado", "unidades",
                             "zanahoria", "xenophobia", "walabi", "semaforo", "corporal"]
        self.palabra = ""
        self.userPalabra = ""
        self.errores = 0

        self.reiniciar()
        #Signals
        self.btnReset.clicked.connect(self.reiniciar)
        self.btnVer.clicked.connect(self.verLetra)

    #Slots
    def reiniciar(self):
        self.palabra = self.listPalabras[random.randrange(0, 10)]
        self.userPalabra = ""
        for i in self.palabra:
            self.userPalabra += "_"
        self.txtLetra.setText("")
        self.lbRope.setText("")
        self.lbHead.setText("")
        self.lbBody.setText("")
        self.lbLegs.setText("")
        print(self.palabra)
        self.mostrarPalabra()

    def mostrarPalabra(self):
        linea = ""
        for i in self.userPalabra:
            linea += i + " "
        print(self.userPalabra)
        self.lbPalabra.setText(linea)

    def verLetra(self):
        letra = self.txtLetra.text()
        e = False
        c = 0
        for i in self.palabra:
            if letra == i:
                self.userPalabra = self.userPalabra[:c] + letra + self.userPalabra[c + 1:]
                e = True
            c += 1
        if not e:
            self.errores += 1
        self.mostrarPalabra()
        print("errores = ",self.errores)
        if self.userPalabra == self.palabra:
            self.mensaje("Gano el juego!")
            self.reiniciar()
        else:
            self.ahorcado()
            self.txtLetra.setText("")

    def ahorcado(self):
        match self.errores:
            case 1: self.lbRope.setText("|")
            case 2: self.lbHead.setText("O")
            case 3: self.lbBody.setText(" |")
            case 4: self.lbBody.setText("/|")
            case 5: self.lbBody.setText("/|\\")
            case 6: self.lbLegs.setText("/")
            case 7:
                    self.lbLegs.setText("/\\")
                    self.mensaje("Fin del juego")
                    self.reiniciar()

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
