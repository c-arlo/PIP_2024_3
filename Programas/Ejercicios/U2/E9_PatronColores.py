import random
import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E9_PatronColores.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.listBtns = [self.btnR, self.btnG, self.btnB, self. btnY]
        self.diccColor = {
            -1: "background-color: rgb(100, 0, 0); border-radius:60px;", #rojo apagado
            -2: "background-color: rgb(0, 100, 0); border-radius:60px;", #verde apagado
            -3: "background-color: rgb(0, 0, 100); border-radius:60px;", #azul apagado
            -4: "background-color: rgb(100, 100, 0); border-radius:60px;", #amarillo apagado
            0: "background-color: rgb(0, 0, 0); border-radius:60px;", #negro
            1: "background-color: rgb(255, 0, 0); border-radius:60px;", #rojo
            2: "background-color: rgb(0, 255, 0); border-radius:60px;", #verde
            3: "background-color: rgb(0, 0, 255); border-radius:60px;", #azul
            4: "background-color: rgb(255, 255, 0); border-radius:60px;" #amarillo
        }
        self.randColores = []
        self.userColores = []
        self.score = 0
        self.showColor = 0
        self.index = 0
        self.hiloSeg = QtCore.QTimer()
        self.hiloPatron = QtCore.QTimer()

        self.hiloSeg.setSingleShot(True)
        self.btnsEnabled(False)

        #Signals
        self.hiloSeg.timeout.connect(self.btnTick)
        self.hiloPatron.timeout.connect(self.updatePatron)
        self.btnStart.clicked.connect(self.start)
        for i in self.listBtns:
            i.clicked.connect(self.cambiarColor)

    #Slots
    def cambiarColor(self):
        obj = self.sender()
        s = 0
        match obj.objectName():
            case "btnR":
                obj.setStyleSheet(self.diccColor[1])
                s = 1
            case "btnG":
                obj.setStyleSheet(self.diccColor[2])
                s = 2
            case "btnB":
                obj.setStyleSheet(self.diccColor[3])
                s = 3
            case "btnY":
                obj.setStyleSheet(self.diccColor[4])
                s = 4
        self.userColores.append(s)
        self.hiloSeg.start(150)
        print(self.userColores)
        if len(self.userColores) == len(self.randColores):
            if self.userColores == self.randColores:
                self.score += 1
                self.txtScore.setText(str(self.score))
                self.userColores = []
                self.btnsEnabled(False)
                self.genPatron()
            else:
                self.mensaje("EQUIVOCADO FIN DEL JUEGO")
                self.start()

    def btnTick(self):
        self.btnR.setStyleSheet(self.diccColor[-1])
        self.btnG.setStyleSheet(self.diccColor[-2])
        self.btnB.setStyleSheet(self.diccColor[-3])
        self.btnY.setStyleSheet(self.diccColor[-4])
        self.hiloSeg.stop()

    def updatePatron(self):
        if self.index < len(self.randColores) and self.showColor == 0:
            print("index = ", str(self.index))
            self.showColor = self.randColores[self.index]
            self.index += 1
        elif self.showColor != 0:
            self.showColor = 0
        else:
            self.index = 0
            self.hiloPatron.stop()
            self.btnsEnabled(True)
            self.inst.setText("Repite el patrón de colores mostrado en la parte superior")
        self.color.setStyleSheet(self.diccColor[self.showColor])

    def genPatron(self):
        self.inst.setText("Pon atencion al patron")
        self.randColores.append(random.randrange(1, 5))
        print(self.randColores, " len = ", len(self.randColores))
        self.hiloPatron.start(400)


    def start(self):
        t = self.btnStart.text()
        if t == "Iniciar":
            self.btnStart.setText("Reiniciar")
            self.genPatron()
        else:
            self.btnsEnabled(False)
            self.btnStart.setText("Iniciar")
            self.score = 0
            self.txtScore.setText(str(self.score))
            self.userColores = []
            self.randColores = []

    def btnsEnabled(self, B):
        for i in self.listBtns:
            i.setEnabled(B)

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
