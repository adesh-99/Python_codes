import speech_recognition as sr
from moviepy.editor import VideoFileClip
from PyQt5 import QtWidgets
import sys
import tkinter as tk
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtGui import *
import time
from os import path
from pydub import AudioSegment
import subprocess


def output_name(name):
    name = name.split("/")[-1]
    name = name.split(".")[0]
    return name + ".mp3"


def output_namee(name):
    name = name.split("/")[-1]
    name = name.split(".")[0]
    return name + ".wav"


def convert1(mp4):
    mp3_file = output_name(mp4)
    videoclip = VideoFileClip(mp4)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()

def convert(mp4):
    wav_file = output_namee(mp4)
    videoclip = VideoFileClip(mp4)
    audioclip = videoclip.audio
    audioclip.write_audiofile(wav_file)
    audioclip.close()
    videoclip.close()


class Convertmp(QtWidgets.QWidget):
    def _init_(self):
        self._start_time = None
        super(Convertmp,self)._init_()
        self.initUI()
        oImage = QImage("C:/Users/91927/Dropbox/PC/Documents/gui interface.png")   #background image
        sImage = oImage.scaled(QSize(1910, 1050))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def initUI(self):
        self.setGeometry(5, 50, 1980, 1000)
        self.setWindowTitle("Video To Audio,Audio To Text Convertor")
        self.bg="black"

        self.label = QLabel('                                                      ', self)   #label before button clicked
        self.label.setFont(QFont('Arial Rounded MT Bold', 20, ))
        self.label.move(740, 430)
        self.label1 = QLabel('            Welcome    \n      Browse Videos...              ', self)
        self.label1.move(160, 430)
        self.label1.setFont(QFont('Arial Rounded MT Bold', 20, ))
        self.label2 = QLabel('                                                                                   ', self)
        self.label2.move(670, 800)
        self.label2.setFont(QFont('Arial Rounded MT Bold', 20, ))
        self.label3 = QLabel('                                                             ',self)
        self.label3.setFont(QFont('Arial Rounded MT Bold', 16, ))
        self.label3.move(1350, 540)
        self.label_filename = QLabel('Filename :                                                                             Filename :                                                                                    Filename :',self)
        self.label_filename.move(85, 600)
        self.label_filename.setFont(QFont('Elephant', 14))
        self.label_filename1 = QLabel('                                                                                  ', self)
        self.label_filename1.move(220, 600)
        self.label_filename1.setFont(QFont('Bahnschrift', 14))
        self.label6 = QLabel('                                                ',self)
        self.label6.setFont(QFont('Calibri', 20))
        self.label6.move(765, 855)
        self.label5 = QLabel("                                                                              ",self)
        self.label5.setFont(QFont('Bahnschrift', 14))
        self.label5.move(800, 600)
        self.label7 = QLabel("                                                                              ", self)
        self.label7.setFont(QFont('Bahnschrift', 14))
        self.label7.move(1430, 600)

#------------------------------------------------------------------------------------------------------------------------
                                                     #Buttons

        # self.setStyleSheet("background:red")
        btn = QtWidgets.QPushButton("BROWSE VIDEO", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setGeometry(114, 245, 446, 125)
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.setToolTip('Click to import video')
        btn.clicked.connect(self.Browse)
        btn.clicked.connect(self.label_show1)

        btn = QtWidgets.QPushButton("CONVERT TO AUDIO", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setGeometry(730, 245, 446, 125)
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.setToolTip('Click to covert into audio')

        btn.clicked.connect(self.label_show)


        btn = QtWidgets.QPushButton("WAV", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.setGeometry(755, 510, 150, 40)
        btn.setToolTip('Click to Convert into Wav')
        btn.clicked.connect(self.conve)
        btn.clicked.connect(self.label_show2)

        self.btn = QtWidgets.QPushButton("MP3", self)
        self.btn.setFont(QFont('Arial Rounded MT Bold', 13))
        self.btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        self.btn.setGeometry(1010, 510, 150, 40)
        self.btn.clicked.connect(self.conv)
        self.btn.clicked.connect(self.label_show2)

        btn = QtWidgets.QPushButton("AUDIO TO TEXT", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setGeometry(1370,245, 446, 125)
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.setToolTip('Click to covert into Text')

        btn = QtWidgets.QPushButton("WAV", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.setGeometry(1650, 450, 150, 40)
        btn.setToolTip('Click to Convert into Wav')
        '''btn.setStyleSheet("border-radius : 50;border : 2px solid black")
        btn.setGeometry(200, 150, 100, 100)'''       #circle button
        btn.clicked.connect(self.text)
        btn.clicked.connect(self.label_show3)


        btn = QtWidgets.QPushButton("MP3", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setGeometry(1400,450, 150, 40)
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.setToolTip('Click to covert into MP3')
        btn.clicked.connect(self.texteng)
        btn.clicked.connect(self.label_show3)

        btn = QtWidgets.QPushButton(" MARATHI AUDIO TO TEXT", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setGeometry(1385, 680, 400, 100)
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.setToolTip('Click to convert into Text')
        btn.clicked.connect(self.textmar)
        btn.clicked.connect(self.label_show3)
        #btn.clicked.connect(self.show_infoo_messagebox)


        btn = QtWidgets.QPushButton("WAV", self)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setToolTip('Click to covert into Wav')
        btn.setGeometry(1395,830, 150, 40)
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")          #making buttons for diffrent extensions to import the audio to convert into  text
        btn.clicked.connect(self.textmar)
        btn.clicked.connect(self.label_show3)

        btn = QtWidgets.QPushButton("MP3", self)
        btn.setGeometry(1625, 830, 150,40)
        btn.setFont(QFont('Arial Rounded MT Bold', 13))
        btn.setToolTip('Click to covert into MP3')
        btn.setStyleSheet("border : 2px solid black;border-radius : 20px;")
        btn.clicked.connect(self.textmarathi)
        btn.clicked.connect(self.label_show3)
        self.show()


    def Browse(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Single File", "*.mp4")
        self.c = filepath[0]
        print("Filepath: ", self.c)
        self.label_filename1.setText(str(self.c[36:]))

    def label_show(self):
        self.label.setText('Please Select the file type !')            #label displayed on button clicked
    def label_show1(self):
        self.label1.setText('  Video is Imported\n  Ready to Convert...')
    def label_show2(self):
        self.label2.setText('Your Video is Converted into Audio')
    def label_show3(self):
        self.label3.setText('Audio is Converted into Text')

    def show_infoo_messagebox(self):                           #confirmation message after converting to audio.
        a = QLabel('Convert Vedio to Audio ', self)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setGeometry(680, 440, 400, 300)

        # setting message for Message Box
        msg.setText("your audio is converted in text. ")

        # setting Message box window title
        msg.setWindowTitle("convertor")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # start the app
        retval = msg.exec_()


    def conv(self):
        self.start_time = time.time()

        try:
            convert1(self.c)
            output_name(self.c)
            self.label5.setText(output_name(self.c))
        except:
            pass
        self.end_time = time.time()
        self.time_lapsed = self.end_time - self.start_time
        self.time_convert(self.time_lapsed)

    def conve(self):
        self.start_time = time.time()
        try:
            convert(self.c)
            output_namee(self.c)
            self.label5.setText(output_namee(self.c))
        except:
            pass
        self.end_time = time.time()

        self.time_lapsed = self.end_time - self.start_time
        self.time_convert(self.time_lapsed)

    def text(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Single File", "*.wav",)
        self.c = filepath[0]
        r = sr.Recognizer()
        self.start_time = time.time()
        audio = sr.AudioFile(self.c)
        with audio as source:
            audio_file = r.record(source)

        result = r.recognize_google(audio_file)

        with open('recog.txt', mode='w') as file:
            file.write("speech recognized")
            file.write("\n")
            file.write(result)
            print("Now the file is ready")
            self.label7.setText("recog.txt")
        self.end_time = time.time()

        self.time_lapsed = self.end_time - self.start_time
        self.time_convert(self.time_lapsed)
        filename = "recog.txt"
        subprocess.run(["notepad", filename])

    def texteng(self):
        self.start_time = time.time()
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Single File", "*.mp3")
        self.c = filepath[0]
        sound = AudioSegment.from_mp3(self.c)
        sound.export("transcript.wav", format="wav")

        # transcribe audio file
        AUDIO_FILE = "transcript.wav"

        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
            result = r.recognize_google(audio)
            with open('Marathi_mp3_convert.txt', mode='w') as file:
                file.write("speech recognized....")
                file.write("\n")
                file.write(result)
                print("Now the file is ready")
                self.label7.setText("Marathi_mp3_convert.txt")
        self.end_time = time.time()

        self.time_lapsed = self.end_time - self.start_time
        self.time_convert(self.time_lapsed)
        filename = "Marathi_mp3_convert.txt"
        subprocess.run(["notepad", filename])

    def textmar(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Single File", "*.wav")
        self.c = filepath[0]

        r = sr.Recognizer()
        self.start_time = time.time()
        # specify the path to the Marathi MP3 file
        audio_file = sr.AudioFile(self.c)

        # use the recognizer to read the audio file
        with audio_file as source:
            audio = r.record(source)

        # convert speech to text
        text = r.recognize_google(audio, language="mr-IN")

        # write the text to a file
        with open("Marathi_wav_convert.txt", "w", encoding="utf-8") as file:
            file.write(text)
            self.label7.setText("Marathi_wav_convert.txt")
        self.end_time = time.time()

        self.time_lapsed = self.end_time - self.start_time
        self.time_convert(self.time_lapsed)
        filename = "Marathi_wav_convert.txt"
        subprocess.run(["notepad", filename])

    def textmarathi(self):
        filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Single File", "*.mp3")
        self.c = filepath[0]
        sound = AudioSegment.from_mp3(self.c)
        sound.export("transmarathi.wav", format="wav")

        # transcribe audio file
        AUDIO_FILE = "transmarathi.wav"
        self.start_time = time.time()
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
        text = r.recognize_google(audio, language="mr-IN")

        # write the text to a file
        with open("Marathi_mp3_convert.txt", "r+", encoding="utf-8") as file:
            file.write(text)
            self.label7.setText("Marathi_mp3_convert.txt")
        self.end_time = time.time()

        self.time_lapsed = self.end_time - self.start_time
        self.time_convert(self.time_lapsed)
        filename = "Marathi_mp3_convert.txt"
        subprocess.run(["notepad", filename])

    def time_convert(self, sec):
        self.mins = int(sec // 60)
        self.sec = sec % 60
        self.hours = self.mins // 60
        self.mins = int(self.mins % 60)
        a=("Time Elapsed = {0}:{1}:{2}".format(int(self.hours), int(self.mins), sec))
        self.label6.setText(a)
        print(a)


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Convertmp()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()