import random
import sys
import time

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E8_Memorama.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # clickable(self.img).connect(self.clicImage)
        self.imagenes = {
            # -1: ":/Memorama/Memorama/Desc.png",
            0: ":/Memorama/Memorama/manzana.png",
            1: ":/Memorama/Memorama/pera.png",
            2: ":/Memorama/Memorama/coco.png",
            3: ":/Memorama/Memorama/fresa.png"
        }
        self.btnList = [self.opc1, self.opc2, self.opc3, self.opc4, self.opc5, self.opc6,
                        self.opc7, self.opc8, self.opc9, self.opc10, self.opc11, self.opc12]
        self.score = 0
        self.opcA = -1
        self.opcB = -1
        self.senderA = None
        self.senderB = None
        self.randoImgs = []
        self.loadImagenes()

        self.btnReset.clicked.connect(self.reset)
        self.btnStart.clicked.connect(self.start)
        self.txtScore.textChanged.connect(self.finDeJuego)

        for i in self.btnList:
            i.clicked.connect(self.mostrarCarta)

    def mostrarCarta(self):
        obj = self.sender()
        name = obj.objectName()
        index = -1
        match name:
            case "opc1": index = 0
            case "opc2": index = 1
            case "opc3": index = 2
            case "opc4": index = 3
            case "opc5": index = 4
            case "opc6": index = 5
            case "opc7": index = 6
            case "opc8": index = 7
            case "opc9": index = 8
            case "opc10": index = 9
            case "opc11": index = 10
            case "opc12": index = 11
        obj.setStyleSheet("border-image: url(" + self.imagenes[self.randoImgs[index]] +
                          "); background-color: rgb(255, 255, 255);")
        obj.setEnabled(False)
        if self.opcA == -1:
            self.opcA = self.randoImgs[index]
            self.senderA = obj
        else:
            self.opcB = self.randoImgs[index]
            self.senderB = obj
        #print("opcA = ", self.opcA, " opcB = ", self.opcB)
        #print("senderA = ", self.senderA, " senderB = ", self.senderB)
        if self.opcA != -1 and self.opcB != -1:
            if self.opcA == self.opcB:
                self.mensaje("Correcto!")
                self.score += 1
                self.txtScore.setText(str(self.score))
            else:
                self.mensaje("Incorrecto!")
                self.senderA.setStyleSheet(
                    "border-image: url(:/Memorama/Memorama/Desc.png); background-color: rgb(255, 255, 255);")
                self.senderA.setEnabled(True)
                self.senderB.setStyleSheet(
                    "border-image: url(:/Memorama/Memorama/Desc.png); background-color: rgb(255, 255, 255);")
                self.senderB.setEnabled(True)
                self.score -= 1
                self.txtScore.setText(str(self.score))
            self.opcA = -1
            self.opcB = -1

    def finDeJuego(self):
        if self.score < 0:
            self.mensaje("Fin del juego!")
            self.reset()
        if self.score == 6:
            self.mensaje("Fin del juego!")
            self.reset()

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

    def start(self):
        c = 0
        for i in self.btnList:
            i.setStyleSheet("border-image: url(:/Memorama/Memorama/Desc.png); background-color: rgb(255, 255, 255);")
            i.setEnabled(True)
        self.btnStart.setEnabled(False)

    def loadImagenes(self):
        while True:
            self.randoImgs = []
            for i in range(12):
                self.randoImgs.append(random.randrange(0, 4))
            # print(ranImages)
            impar = False
            for i in self.imagenes:
                # p = "{0} = {1}".format(i, self.randoImgs.count(i))
                # print(p)
                if self.randoImgs.count(i) % 2 != 0 or self.randoImgs.count(i) == 0:
                    impar = True
            if not impar:
                break
        c = 0
        for i in self.btnList:
            i.setStyleSheet("border-image: url(" + self.imagenes[self.randoImgs[c]] +
                            "); background-color: rgb(255, 255, 255);")
            i.setEnabled(False)
            c += 1

    def reset(self):
        self.score = 0
        self.txtScore.setText(str(self.score))
        self.loadImagenes()
        self.btnStart.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
