import random
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E13_AdivinaNum.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.P1Num = 0
        self.CPUNum = 0
        self.P1Guess = 0
        self.CPUGuess = 0
        self.P1Fails = 0
        self.CPUFails = 0

        # Signals
        self.btnStart.clicked.connect(self.start)
        self.btnGuess.clicked.connect(self.P1Adivina)

    # Slots
    def start(self):
        o = self.btnStart.text()
        if o == "Iniciar":
            t = self.txtP1Num.text()
            if self.verRango(t):
                self.P1Num = int(t)
            else:
                self.txtP1Num.setText("")
                return
            self.CPUNum = random.randrange(1, 100)

            self.txtP1Num.setEnabled(False)
            self.txtP1Guess.setEnabled(True)
            self.btnGuess.setEnabled(True)

            self.btnStart.setText("Reiniciar")
        else:
            self.P1Num = 0
            self.CPUNum = 0
            self.P1Guess = 0
            self.CPUGuess = 0
            self.P1Fails = 0
            self.CPUFails = 0

            self.txtP1Num.setText("")
            self.txtP1Guess.setText("")
            self.txtP1Fails.setText("0")

            self.txtP1Num.setEnabled(True)
            self.txtP1Guess.setEnabled(False)
            self.btnGuess.setEnabled(False)

            self.btnStart.setText("Iniciar")

        print("P1Num ", self.P1Num, " / CPUNum ", self.CPUNum)

    def verRango(self, t):
        if t != "":
            n = int(t)
            if n <= 0 or n > 100:
                self.mensaje("Recuerda!\nEl numero debe encontrarse entre 1 y 100")
                return False
            else:
                return True
        else:
            self.mensaje("Recuerda!\nEl numero debe encontrarse entre 1 y 100")
            return False

    def P1Adivina(self):
        t = self.txtP1Guess.text()
        if self.verRango(t):
            self.P1Guess = int(t)
        else:
            self.txtP1Guess.setText("")
            return
        if self.P1Guess == self.CPUNum:
            self.mensaje("Adivinaste el numero del oponente!")
            self.txtP1Guess.setEnabled(False)
            self.btnGuess.setEnabled(False)
            self.txtCPUNum.setText(str(self.CPUNum))
        else:
            self.P1Fails += 1
            self.txtP1Fails.setText(str(self.P1Fails))
            self.txtP1Guess.setText("")
            self.CPUAdivina()
        print("P1Guess ", self.P1Guess, " / CPUNum ", self.CPUNum)

    def CPUAdivina(self):
        self.CPUGuess = random.randrange(1, 100)
        if self.CPUGuess == self.P1Num:
            self.mensaje("El oponente adivino tu numero!")
        else:
            self.CPUFails += 1
        self.txtCPUGuess.setText(str(self.CPUGuess))
        self.txtCPUFails.setText(str(self.CPUFails))

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
