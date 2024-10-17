import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E10_Gato.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.casillas = [self.s1, self.s2, self.s3,
                         self.s4, self.s5, self.s6,
                         self.s7, self.s8, self.s9]
        self.c = ["", "", "",
                  "", "", "",
                  "", "", ""]
        self.diccTurno = {
            1: "X",
            2: "O"
        }
        self.turno = 1
        # Signals
        for i in self.casillas:
            i.setText("")
            i.clicked.connect(self.clickCasilla)
        self.btnReset.clicked.connect(self.reset)

    # Slots
    def clickCasilla(self):
        obj = self.sender()
        match obj.objectName():
            case "s1":
                self.c[0] = self.diccTurno[self.turno]
            case "s2":
                self.c[1] = self.diccTurno[self.turno]
            case "s3":
                self.c[2] = self.diccTurno[self.turno]
            case "s4":
                self.c[3] = self.diccTurno[self.turno]
            case "s5":
                self.c[4] = self.diccTurno[self.turno]
            case "s6":
                self.c[5] = self.diccTurno[self.turno]
            case "s7":
                self.c[6] = self.diccTurno[self.turno]
            case "s8":
                self.c[7] = self.diccTurno[self.turno]
            case "s9":
                self.c[8] = self.diccTurno[self.turno]
        obj.setText(self.diccTurno[self.turno])
        obj.setEnabled(False)
        if self.turno == 1:
            obj.setStyleSheet("font: 36pt \"Comic Sans MS\";"
                              "background-color: rgb(255, 255, 255);"
                              "color: rgb(0, 0, 255)")
            self.turno = 2
            self.lbTurno.setText("Jugador 2 (O)")
            self.lbTurno.setStyleSheet("font: 75 20pt \"Comic Sans MS\";"
                                       "color: rgb(255, 0, 0);")
        else:
            self.turno = 1
            self.lbTurno.setText("Jugador 1 (X)")
            obj.setStyleSheet("font: 36pt \"Comic Sans MS\";"
                              "background-color: rgb(255, 255, 255);"
                              "color: rgb(255, 0, 0)")
            self.lbTurno.setStyleSheet("font: 75 20pt \"Comic Sans MS\";"
                                       "color: rgb(0, 0, 255);")
        self.matches()

    def matches(self):
        wMatches = [[self.c[0], self.c[1], self.c[2]],
                    [self.c[0], self.c[4], self.c[8]],
                    [self.c[0], self.c[3], self.c[6]],
                    [self.c[1], self.c[4], self.c[7]],
                    [self.c[2], self.c[5], self.c[8]],
                    [self.c[2], self.c[4], self.c[6]],
                    [self.c[3], self.c[4], self.c[5]],
                    [self.c[6], self.c[7], self.c[8]]]
        for i in wMatches:
            linea = ""
            for j in i:
                linea += j
            if linea == "XXX":
                self.mensaje("El ganador es el Jugador 1")
                self.reset()
            elif linea == "OOO":
                self.mensaje("El ganador es el Jugador 2")
                self.reset()

    def reset(self):
        self.c = ["", "", "",
                  "", "", "",
                  "", "", ""]
        for i in self.casillas:
            i.setText("")
            i.setEnabled(True)
        self.turno = 1
        self.lbTurno.setText("Jugador 1 (X)")
        self.lbTurno.setStyleSheet("font: 75 20pt \"Comic Sans MS\";"
                                   "color: rgb(0, 0, 255);")

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
