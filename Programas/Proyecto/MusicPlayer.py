import sys
import time
import serial as ser
from PyQt5 import uic, QtWidgets, QtCore
#from PyQt5.QtCore import QThread, pyqtSignal
from tkinter import filedialog
from pygame import mixer

qtCreatorFile = "MusicPlayer.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.songList = []
        self.songDir = {}

        self.paused = False
        self.mute = False

        self.index = 0
        self.vol = 100
        self.milsecs = 0
        self.secs = 0
        self.mins = 0

        mixer.init()
        self.time = QtCore.QTimer()
        self.arduinoTimer = QtCore.QTimer()
        self.arduino = None

        # Área de los Signals
        self.btnAddSong.clicked.connect(self.addSong)
        self.btnPlay.clicked.connect(self.play)
        self.btnPause.clicked.connect(self.pause)
        self.btnStop.clicked.connect(self.stop)
        self.btnNext.clicked.connect(self.skipSong)
        self.btnPrev.clicked.connect(self.prevSong)
        self.btnMute.clicked.connect(self.muted)
        self.btnArduino.clicked.connect(self.connectArduino)
        self.sliderVol.valueChanged.connect(self.volume)
        self.time.timeout.connect(self.playTime)
        self.arduinoTimer.timeout.connect(self.readArduino)

        self.arduinoTimer.start(1)
    # Área de los Slots

    def connectArduino(self):
        if self.arduino is None:
            try:
                self.arduino = ser.Serial(port="COM6", baudrate=9600, timeout=0.1)
            except Exception as e:
                m = QtWidgets.QMessageBox()
                m.setText(str(e) + "\n\nERROR: No se encuentra un dispositivo conectado")
                m.exec()
                return
            self.btnArduino.setText("✅")
        else:
            self.arduino = None
            self.btnArduino.setText("⚠️")

    def muted(self):
        if not self.mute:
            self.mute = True
            self.vol = 0
            self.txtVol.setText("MUTE")
            self.btnMute.setText("🔇")
        else:
            self.mute = False
            self.vol = self.sliderVol.value()
            self.txtVol.setText(str(self.vol))
            self.btnMute.setText("🔊")
        mixer.music.set_volume(self.vol / 100)

    def volume(self):
        self.btnMute.setText("🔊")
        self.mute = False
        self.vol = self.sliderVol.value()
        self.txtVol.setText(str(self.vol))
        mixer.music.set_volume(self.vol / 100)

    def addSong(self):
        f = filedialog.askopenfilename(initialdir='/Downloads',
                                       title='Selecciona un archivo',
                                       filetypes=[(".mp3", ".mp3")]
                                       )
        if f != "":
            n = f.split("/")[-1].split(".")[0]
            self.songList.append(n)
            self.songDir[n] = f
            self.listSongs.addItem(str(len(self.songList)) + ".- " + n)

    def writeArduino(self, cadena):
        if self.arduino is not None and self.arduino.isOpen():
            #c = str(self.index + 1) + ".- " + self.songList[self.index]
            self.arduino.write(cadena.encode())

    def readArduino(self):
        if self.arduino is not None and self.arduino.isOpen():
            try:
                c = self.arduino.readline().decode().strip()
                if c != "":
                    if "V/" in c:
                        self.sliderVol.setValue(int(c.split("/")[1]))
                    elif "PLAY" in c:
                        self.play()
                    elif "PAUSE" in c:
                        self.pause()
                    elif "PREV" in c:
                        self.prevSong()
                    elif "NEXT" in c:
                        self.skipSong()
            except Exception as e:
                print(e)

    def play(self):
        if len(self.songList) == 0:
            return
        if self.paused:
            mixer.music.unpause()
            self.paused = False
            self.writeArduino("T/PLAY")
            self.time.start(1)
        else:
            self.txtIndex.setText(str(self.index + 1))
            self.txtTitle.setText(self.songList[self.index])
            cadena = "M/" + str(self.index + 1) + ".- " + self.songList[self.index]
            self.writeArduino(cadena)
            time.sleep(0.3)
            self.writeArduino("T/PLAY")
            mixer.music.load(self.songDir[self.songList[self.index]])
            mixer.music.play()
            self.time.start(1)

    def pause(self):
        if len(self.songList) == 0:
            return
        mixer.music.pause()
        self.time.stop()
        self.paused = True
        self.writeArduino("T/PAUSE")

    def nextSong(self):
        if not self.paused and not mixer.music.get_busy():
            self.resetTimer()
            self.index += 1
            if self.index == len(self.songList):
                self.index = 0
            self.play()

    def stop(self):
        mixer.music.stop()
        self.resetTimer()
        self.txtTitle.setText("")
        self.index = 0
        self.paused = False
        self.txtIndex.setText("")
        self.writeArduino("T/STOP")

    def skipSong(self):
        if len(self.songList) == 0:
            return
        self.paused = False
        mixer.music.stop()
        self.nextSong()

    def prevSong(self):
        if len(self.songList) == 0:
            return
        self.paused = False
        mixer.music.stop()
        self.resetTimer()
        if self.index - 1 < 0:
            self.index = len(self.songList) - 1
        else:
            self.index -= 1
        self.play()

    def resetTimer(self):
        self.time.stop()
        self.milsecs = 0
        self.secs = 0
        self.mins = 0
        self.txtSecs.setText("00")
        self.txtMins.setText("00")
        self.writeArduino("T/RESET")

    def playTime(self):
        self.milsecs += 1
        if self.milsecs == 1000:
            self.milsecs = 0
            self.secs += 1
            if self.secs > 59:
                self.mins += 1
                self.secs = 0
                if self.mins < 10:
                    self.txtMins.setText("0" + str(self.mins))
                elif self.secs > 9:
                    self.txtMins.setText(str(self.mins))
            if self.secs < 10:
                self.txtSecs.setText("0" + str(self.secs))
            elif self.secs > 9:
                self.txtSecs.setText(str(self.secs))
        self.nextSong()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
