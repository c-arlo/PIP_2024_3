import random
import sys

import pygame
from PyQt5 import uic, QtWidgets, QtCore
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
        self.vol = 0
        self.milsecs = 0
        self.secs = 0
        self.mins = 0

        mixer.init()
        self.time = QtCore.QTimer()

        # Área de los Signals
        self.btnAddSong.clicked.connect(self.addSong)
        self.btnPlay.clicked.connect(self.play)
        self.btnPause.clicked.connect(self.pause)
        self.btnStop.clicked.connect(self.stop)
        self.btnNext.clicked.connect(self.skipSong)
        self.btnPrev.clicked.connect(self.prevSong)
        self.btnMute.clicked.connect(self.muted)
        self.btnShuffle.clicked.connect(self.shuffle)
        self.sliderVol.valueChanged.connect(self.volume)
        self.time.timeout.connect(self.playTime)

    # Área de los Slots
    def shuffle(self):
        if len(self.songList) == 0:
            return
        random.shuffle(self.songList)
        self.listSongs.clear()
        c = 1
        for i in self.songList:
            self.listSongs.addItem(str(c)+".- "+i)
            c += 1
        self.stop()


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
        mixer.music.set_volume(self.vol/100)

    def addSong(self):
        f = filedialog.askopenfilename(initialdir='/',
                                       title='Selecciona una archivo',
                                       filetypes=[(".mp3", ".mp3")]
                                       )
        if f != "":
            n = f.split("/")[-1].split(".")[0]
            self.songList.append(n)
            self.songDir[n] = f
            self.listSongs.addItem(str(len(self.songList))+".- "+n)

    def play(self):
        if len(self.songList) == 0:
            return
        if self.paused:
            mixer.music.unpause()
            self.paused = False
            self.time.start(1)
        else:
            self.txtIndex.setText(str(self.index+1))
            self.txtTitle.setText(self.songList[self.index])
            mixer.music.load(self.songDir[self.songList[self.index]])
            mixer.music.play()
            self.time.start(1)

    def pause(self):
        if len(self.songList) == 0:
            return
        mixer.music.pause()
        self.time.stop()
        self.paused = True

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
        if self.index-1 < 0:
            self.index = len(self.songList)-1
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

    def playTime(self):
        self.nextSong()
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
