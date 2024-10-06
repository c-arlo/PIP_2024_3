import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E4_Semaforo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.lbl_stop.setStyleSheet("color: rgb(100, 0, 0);")
        self.lbl_wait.setStyleSheet("color: rgb(139, 100, 0);")
        self.lbl_go.setStyleSheet("color: rgb(0, 100, 0);")

        self.seg = 0
        self.hiloSeg = QtCore.QTimer()
        self.hiloSeg.start(1000)
        self.hiloSeg.timeout.connect(self.contarSeg)

    # Área de los Slots
    def contarSeg(self):
        if self.seg <= 5:
            self.lbl_stop.setStyleSheet("color: rgb(255, 0, 0);")
            self.lbl_wait.setStyleSheet("color: rgb(139, 100, 0);")
            self.lbl_go.setStyleSheet("color: rgb(0, 100, 0);")
            self.seg += 1
        elif 5 <= self.seg <= 8:
            self.lbl_stop.setStyleSheet("color: rgb(100, 0, 0);")
            self.lbl_wait.setStyleSheet("color: rgb(255, 183, 0);")
            self.lbl_go.setStyleSheet("color: rgb(0, 100, 0);")
            self.seg += 1
        elif 8 <= self.seg <= 11:
            self.lbl_stop.setStyleSheet("color: rgb(100, 0, 0);")
            self.lbl_wait.setStyleSheet("color: rgb(139, 100, 0);")
            self.lbl_go.setStyleSheet("color: rgb(0, 255, 0);")
            self.seg += 1
        elif self.seg >= 11:
            self.seg = 0
        print(self.seg)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

