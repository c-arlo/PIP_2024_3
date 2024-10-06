import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E3_Temporizador.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.sb_min.setMinimum(0)
        self.sb_min.setMaximum(59)
        self.sb_min.setSingleStep(1)
        self.sb_min.setValue(0)

        self.sb_seg.setMinimum(0)
        self.sb_seg.setMaximum(59)
        self.sb_seg.setSingleStep(1)
        self.sb_seg.setValue(0)

        self.segundos = 0
        self.minutos = 0

        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_reset.clicked.connect(self.reset)

        self.hiloSeg = QtCore.QTimer()
        self.hiloSeg.timeout.connect(self.contarSeg)

    # Área de los Slots
    def reset(self):
        self.hiloSeg.stop()
        self.segundos = 0
        self.minutos = 0
        self.sb_seg.setValue(self.segundos)
        self.sb_min.setValue(self.minutos)
        self.btn_iniciar.setText("INICIAR")
        self.sb_min.setEnabled(True)
        self.sb_seg.setEnabled(True)

    def iniciar(self):
        self.segundos = self.sb_seg.value()
        self.minutos = self.sb_min.value()
        if self.btn_iniciar.text() == "INICIAR":
            self.btn_iniciar.setText("DETENER")
            self.sb_min.setEnabled(False)
            self.sb_seg.setEnabled(False)
            self.hiloSeg.start(100)  # 1 seg
        else:
            self.sb_min.setEnabled(True)
            self.sb_seg.setEnabled(True)
            self.hiloSeg.stop()
            self.btn_iniciar.setText("INICIAR")


    def contarSeg(self):
        #print(self.valor_inicial)
        self.sb_seg.setValue(self.segundos)
        self.segundos -= 1
        if self.segundos == -1:
            if self.minutos == 0:
                self.hiloSeg.stop()
                self.mensaje("Termino")
                self.iniciar()
            else:
                self.minutos -= 1
                self.sb_min.setValue(self.minutos)
            self.segundos = 59

    def mensaje(self,texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

