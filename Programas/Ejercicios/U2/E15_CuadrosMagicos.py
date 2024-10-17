import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E15_CuadrosMagicos.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.cuadros = [self.c0, self.c1, self.c2,
                        self.c3, self.c4, self.c5,
                        self.c6, self.c7, self.c8]
        self.nums = [0, 0, 0,
                     0, 0, 0,
                     0, 0, 0]

        # Signals
        for i in self.cuadros:
            i.editingFinished.connect(self.numRepetidos)
        self.btnReset.clicked.connect(self.reset)

    # Slots
    def numRepetidos(self):
        obj = self.sender()
        if obj.text() != "" and obj.text() != "-":
            for i in self.cuadros:
                if i.text() == obj.text() and i != obj:
                    obj.setText("")
                    return
            self.nums[self.cuadros.index(obj)] = int(obj.text())
            self.soluciones()
        else:
            self.lbConf.setText("No es un cuadro mágico")


    def soluciones(self):
        lineas = [[self.nums[0], self.nums[1], self.nums[2]],
                  [self.nums[3], self.nums[4], self.nums[5]],
                  [self.nums[6], self.nums[7], self.nums[8]],
                  [self.nums[0], self.nums[4], self.nums[8]],
                  [self.nums[2], self.nums[5], self.nums[8]],
                  [self.nums[1], self.nums[4], self.nums[7]],
                  [self.nums[0], self.nums[3], self.nums[6]],
                  [self.nums[2], self.nums[4], self.nums[6]]]
        sumas = []
        for i in lineas:
            s = 0
            for j in i:
                s += j
            sumas.append(s)
        if sumas.count(sumas[0]) == 8:
            self.lbConf.setText("Número mágico: "+str(sumas[0]))
        else:
            self.lbConf.setText("No es un cuadro mágico")

    def reset(self):
        for i in self.cuadros:
            i.setText("")
            self.lbConf.setText("No es un cuadro mágico")

    def mensaje(self, texto):
        m = QtWidgets.QMessageBox()
        m.setText(texto)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
