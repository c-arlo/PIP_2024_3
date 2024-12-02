import sys
import time

import serial as ser
from PyQt5 import uic, QtWidgets, QtCore
from tkinter import filedialog
from pygame import mixer

qtCreatorFile = "MusicPlayerV2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.songs = []
        self.songsDir = {}

        self.paused = True
        self.mute = False

        self.index = 0
        self.vol = 100
        self.msecs = 0
        self.secs = 0

        mixer.init()
        self.arduino = None

        # Área de los Signals
        self.btnAddSong.clicked.connect(self.addSong)
        self.btnPlay.clicked.connect(self.play)
        self.btnStop.clicked.connect(self.stop)
        self.btnNext.clicked.connect(self.skipSong)
        self.btnPrev.clicked.connect(self.prevSong)
        self.btnMute.clicked.connect(self.muted)
        self.btnRewind.clicked.connect(self.rewind)
        self.btnArduino.clicked.connect(self.connectArduino)

        self.sliderVol.valueChanged.connect(self.setVolume)
        self.sliderPlayT.sliderPressed.connect(self.stopSongPos)
        self.sliderPlayT.sliderReleased.connect(self.setSongPos)

        self.playTimer = QtCore.QTimer()
        self.arduinoTimer = QtCore.QTimer()

        self.playTimer.timeout.connect(self.setPlayTime)
        self.arduinoTimer.timeout.connect(self.readArduino)

    # Área de los Slots
    def addSong(self):
        f = filedialog.askopenfilename(initialdir='/Downloads',
                                       title='Selecciona un archivo',
                                       filetypes=[(".mp3", ".mp3")]
                                       )
        if f != "":
            n = f.split("/")[-1].split(".")[0]
            self.songs.append(n)
            self.songsDir[n] = f
            self.listSongs.addItem(str(len(self.songs)) + ".- " + n)
            if len(self.songs) != 0:
                self.rewind()
                self.btnPlay.setEnabled(True)
                self.btnStop.setEnabled(True)
                self.btnNext.setEnabled(True)
                self.btnPrev.setEnabled(True)
                self.btnRewind.setEnabled(True)
                self.sliderPlayT.setEnabled(True)

    def connectArduino(self):
        if self.arduino is None:
            try:
                self.arduino = ser.Serial(port="COM6", baudrate=9600, timeout=0.01)
            except Exception as e:
                m = QtWidgets.QMessageBox()
                m.setText("⚠ ERROR: No se encuentra un dispositivo conectado")
                m.exec()
                return
            self.btnArduino.setText("✔")
            self.txtArduino.setText("Conectado")
            self.arduinoTimer.start(2)
        else:
            self.arduino = None
            self.btnArduino.setText("🔌")
            self.txtArduino.setText("Desconectado")

    def play(self):
        if not self.paused:
            mixer.music.pause()
            self.btnPlay.setText("►")
            self.paused = True
            self.playTimer.stop()
            time.sleep(0.1)
            self.writeArduino("T/PAUSE")
        else:
            mixer.music.unpause()
            self.btnPlay.setText("II")
            self.paused = False
            self.playTimer.start(2)
            time.sleep(0.1)
            self.writeArduino("T/PLAY")

    def setSong(self):
        c = str(self.index + 1) + ".- " + self.songs[self.index]
        self.txtSong.setText(c)
        self.writeArduino("M/" + c)
        mixer.music.load(self.songsDir[self.songs[self.index]])
        s = mixer.Sound(self.songsDir[self.songs[self.index]]).get_length()
        l = ""
        if s / 60 < 10:
            l += "0" + str(int(s / 60))
        else:
            l += str(int(s / 60))
        l += " : "
        if s % 60 < 10:
            l += "0" + str(int(s % 60))
        else:
            l += str(int(s % 60))
        self.txtSongLen.setText(l)
        self.sliderPlayT.setMaximum(int(s))
        self.sliderPlayT.setValue(0)
        mixer.music.play()
        mixer.music.pause()

    def setPlayTime(self):
        self.msecs += 1
        if self.msecs % 1000 == 0:
            self.secs += 1
        c = ""
        if self.secs/60 < 10:
            c += "0" + str(int(self.secs/60))
        else:
            c += str(int(self.secs/60))
        c += " : "
        if self.secs % 60 < 10:
            c += "0" + str(int(self.secs % 60))
        else:
            c += str(int(self.secs % 60))
        self.txtSongPlayT.setText(c)
        self.sliderPlayT.setValue(self.secs)
        if not self.paused and not mixer.music.get_busy():
            self.skipSong()

    def stopSongPos(self):
        self.playTimer.stop()
        mixer.music.pause()

    def setSongPos(self):
        e = self.sliderPlayT.value()
        self.secs = e
        mixer.music.rewind()
        mixer.music.set_pos(e)
        self.playTimer.start(2)
        mixer.music.unpause()

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

    def setVolume(self):
        self.btnMute.setText("🔊")
        self.mute = False
        self.vol = self.sliderVol.value()
        self.txtVol.setText(str(self.vol))
        mixer.music.set_volume(self.vol / 100)

    def skipSong(self):
        self.resetTimer()
        self.index += 1
        if self.index == len(self.songs):
            self.index = 0
        self.setSong()
        self.paused = True
        self.play()

    def prevSong(self):
        self.resetTimer()
        if self.index - 1 < 0:
            self.index = len(self.songs) - 1
        else:
            self.index -= 1
        self.setSong()
        self.paused = True
        self.play()

    def stop(self):
        self.resetTimer()
        self.index = 0
        self.setSong()
        self.paused = True
        self.btnPlay.setText("►")
        self.writeArduino("T/STOP")
        c = str(self.index + 1) + ".- " + self.songs[self.index]
        time.sleep(0.1)
        self.writeArduino("M/" + c)

    def resetTimer(self):
        mixer.music.stop()
        self.playTimer.stop()
        self.msecs = 0
        self.secs = 0
        self.txtSongPlayT.setText("00 : 00")
        self.writeArduino("T/REWIND")
        time.sleep(0.1)

    def rewind(self):
        self.resetTimer()
        self.setSong()
        mixer.music.rewind()
        self.paused = True
        self.btnPlay.setText("►")
        self.writeArduino("T/REWIND")

    def writeArduino(self, cadena):
        if self.arduino is not None and self.arduino.isOpen():
            # c = str(self.index + 1) + ".- " + self.songList[self.index]
            self.arduino.write(cadena.encode())

    def readArduino(self):
        if self.arduino is not None and self.arduino.isOpen():
            try:
                c = self.arduino.readline().decode().strip()
                if c != "":
                    if "V/" in c:
                        self.sliderVol.setValue(int(c.split("/")[1]))
                    elif "STOP" in c:
                        self.stop()
                    elif "PLAY" in c:
                        self.play()
                    elif "PREV" in c:
                        self.prevSong()
                    elif "NEXT" in c:
                        self.skipSong()
                    elif "REWIND" in c:
                        self.rewind()
                    elif "MUTE" in c:
                        self.muted()
                    elif "VOLDWN" in c:
                        self.sliderVol.setValue(self.vol+10)
                    elif "VOLUP" in c:
                        self.sliderVol.setValue(self.vol-10)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.setStyle("Windows")
    sys.exit(app.exec_())
