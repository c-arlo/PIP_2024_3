import random
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E14_PicasFijas.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.cifras = [self.c1, self.c2, self.c3, self.c4]
        self.usrCifras = [self.a1, self.a2, self.a3, self.a4]
        self.intentos = 1
        self.intentosMax = 4
        self.num = [0, 0, 0, 0]
        self.usrNum = [0, 0, 0, 0]

        # Signals
        self.btnStart.clicked.connect(self.iniciar)
        self.btnAdivinar.clicked.connect(self.adivinar)
        for i in self.cifras:
            i.textChanged.connect(self.verfNums)
        for i in self.usrCifras:
            i.textChanged.connect(self.verfNumsUsr)

    # Slots
    def verfNums(self):
        obj = self.sender()
        if obj.text() == "0":
            obj.setText("")
        if obj.text() != "":
            for i in self.cifras:
                if i.text() == obj.text() and i != obj:
                    obj.setText("")

    def verfNumsUsr(self):
        obj = self.sender()
        if obj.text() == "0":
            obj.setText("")
        if obj.text() != "":
            for i in self.usrCifras:
                if i.text() == obj.text() and i != obj:
                    obj.setText("")

    def iniciar(self):
        if self.btnStart.text() == "Reiniciar":
            self.reiniciar()
        for i in self.cifras:
            if i.text() == "":
                return
            else:
                self.num[self.cifras.index(i)] = int(i.text())
        self.btnStart.setText("Reiniciar")
        print(self.num)
        for i in self.cifras:
            i.setText("")
            i.setEnabled(False)
        self.intentosMax = self.sbTries.value()
        self.sbTries.setEnabled(False)
        self.btnAdivinar.setEnabled(True)
        for i in self.usrCifras:
            i.setEnabled(True)

    def adivinar(self):
        for i in self.usrCifras:
            if i.text() == "":
                return
            else:
                self.usrNum[self.usrCifras.index(i)] = int(i.text())
        print(self.usrNum)
        picas = 0
        fijas = 0
        for i in self.usrNum:
            if i == self.num[self.usrNum.index(i)]:
                fijas += 1
            else:
                for j in self.num:
                    if i == j:
                        picas += 1
        if fijas == 4:
            self.mensaje("El numero fue encontrado!\n"
                         "Intentos: "+str(self.intentos))
            self.btnAdivinar.setEnabled(False)
            for i in self.usrCifras:
                i.setEnabled(False)
        else:
            self.intentos += 1
            self.txtTries.setText(str(self.intentos))
        if self.intentos > self.intentosMax:
            self.mensaje("El numero no fue encontrado!")
            self.btnAdivinar.setEnabled(False)
            for i in self.usrCifras:
                i.setText("")
                i.setEnabled(False)
            self.reiniciar()

        self.txtFijas.setText(str(fijas))
        self.txtPicas.setText(str(picas))

    def reiniciar(self):
        self.btnStart.setText("Iniciar")
        self.txtTries.setText("1")
        self.txtFijas.setText("0")
        self.txtPicas.setText("0")
        self.sbTries.setEnabled(True)
        self.sbTries.setValue(4)
        for i in self.cifras:
            i.setEnabled(True)
        self.btnAdivinar.setEnabled(False)
        for i in self.usrCifras:
            i.setText("")
            i.setEnabled(False)
        self.num = [0, 0, 0, 0]
        self.usrNum = [0, 0, 0, 0]

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
