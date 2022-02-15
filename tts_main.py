from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' Text To Speech')
        self.setGeometry(100, 100, 400, 400)
        self.setWindowIcon(QIcon("python.png"))
        self.setMinimumSize(400,400)
        self.setMaximumWidth(500)
        self.UI()

    def UI(self):

        # adding label
        self.label_text = QLabel("Enter your text below :", self)
        self.label_text.move(80, 60)
        self.label_text.setFont(QFont('Comic Sans MS', 10))

     #   self.label_text.setStyleSheet()

        # adding radio button to switch voice type
        male = QRadioButton("Male Voice", self)
        male.move(100, 350)
        male.setChecked(True)
        male.toggled.connect(self.voice_male)
        female = QRadioButton("Female Voice", self)
        female.move(200, 350)
        female.setChecked(False)
        female.toggled.connect(self.voice_female)

        # adding text field
        self.textEdit = QTextEdit(self)
        self.textEdit.move(80, 100)
        self.textEdit.setStyleSheet("border : 2px solid green;")
        self.textEdit.setStyleSheet( "background-color : beige; border-style : outset ; border-width : 2px; border-radius : 10px; border-color :red; ")

        # adding button to clear text in text field
        clear_button = QPushButton("Clear", self)
        clear_button.move(200, 300)
        clear_button.clicked.connect(self.clear)
        clear_button.setStyleSheet("QPushButton::hover" "{" "background-color : lightgreen;" "}")
        
        # adding button to convert text into speech
        speak_button = QPushButton("Speak", self)
        speak_button.move(100, 300)
        speak_button.clicked.connect(self.gettext)
        speak_button.setStyleSheet("QPushButton::hover" "{" "background-color : lightgreen;" "}" )
        self.show()

    def voice_male(self, selected):
        for voice in voices:
            if selected:
                engine.setProperty('voice', voices[0].id)

    def voice_female(self, selected):
        for voice in voices:
            if selected:
                engine.setProperty('voice', voices[1].id)

    def clear(self):

        self.textEdit.setText(" ")

    def gettext(self):
        text = self.textEdit.toPlainText()

        speak = engine
        speak.say(text)
        speak.runAndWait()


# Creating an instance of QApplication

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


main()
