import sys
from PyQt5 import uic, QtWidgets, QtCore
import Ventana_AgregarAlumno, Ventana_CalcularPromedio, Ventana_VisualizarDatos

##########################################################################

qtCreatorFile1 = "Main_Promedio.ui"  # Nombre del archivo aquí.
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.datosAlumnos = []
        self.index = None
        self.usuario = None

        self.btnAlumno.clicked.connect(self.agregarAlumno)
        self.btnParciales.clicked.connect(self.agregarParciales)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnVisual.clicked.connect(self.visualizar)

        self.listAlumnos.itemClicked.connect(self.cambioUsuario)

    # Área de los Slots
    def visualizar(self):
        self.dialogo = Ventana_VisualizarDatos.MyDialog(self)  # Mandar referencia de la main window
        self.dialogo.setModal(True)
        self.dialogo.show()

    def guardar(self):
        archivo = open("respaldo_interno.sebas", "w")
        for alumno in self.datosAlumnos:
            archivo.write(alumno[0] + "/")
            for par in alumno[1]:
                archivo.write(str(par) + "/")
            archivo.write(str(alumno[2]))
            archivo.write("\n")
        archivo.flush()
        archivo.close()
        print("Archivo guardado")

    def agregarAlumno(self):
        self.dialogo = Ventana_AgregarAlumno.MyDialog(self) #Mandar referencia de la main window
        self.dialogo.setModal(True)
        self.dialogo.show()

    def cambioUsuario(self):
        self.usuario = self.sender().currentItem().text()
        self.index = self.sender().currentRow()

    def agregarParciales(self):
        if not self.usuario is None:
            #index = self.sender().currentItem()

            self.dialogo = Ventana_CalcularPromedio.MyDialog(self)  # Mandar referencia de la main window
            #self.dialogo.lblNombre.setText(self.usuario)
            self.dialogo.setModal(True)
            self.dialogo.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
