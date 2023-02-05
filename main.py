import sys
from PyQt5 import QtWidgets, uic


class MorseTranslator:
    """
    A class used to translate text messages to morse code strings.
    """

    def __init__(self):
        self.morse_code_dictionary = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-',
            'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--',
            'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.',
            '0': '-----', ', ': '--..--', '.': '.-.-.-',
            '?': '..--..', '/': '-..-.', '-': '-....-',
            '(': '-.--.', ')': '-.--.-', ' ': ' '
        }

    def translate_to_morse(self, text_message):
        """
        Translates the message passed from text to morse code.

        Pameters,
        ----------
        text_message : A string containing the message to be converted.
        return : A string with the morse code translation.
        """

        message = text_message.upper()
        morse_message = ""

        try:
            for character in message:
                morse_message = morse_message + " " + self.morse_code_dictionary[str(character)]

        except:
            morse_message = "An invalid character was present, please try again."

        finally:
            return morse_message

def to_morse_button():
    morse_translator = MorseTranslator()
    input_data = window.textInput.toPlainText()
    morse_message = morse_translator.translate_to_morse(input_data)
    window.textOutput.setPlainText(morse_message)


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("GUI.ui")
window.translateButton.clicked.connect(to_morse_button)

window.show()
app.exec()

#

#message = input("What message would you like to translate? ")
#
#print(morse_message)

