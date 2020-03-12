from PyQt5 import QtWidgets, uic



# Function to translate plain text
def rot_13():
    rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    text = str(dig.plain_text.toPlainText())
    dig.cipher_text.setPlainText(str(text.translate(rot13trans)))

#Transposition Cipher
def Trans():
    def split_len(seq, length):
        return [seq[i:i + length] for i in range(0, len(seq), length)]

    def encode(key, plaintext):
        order = {
            int(val): num for num, val in enumerate(key)
        }

        ciphertext = ''
        for index in sorted(order.keys()):
            for part in split_len(plaintext, len(key)):
                try:
                    ciphertext += part[order[index]]
                except IndexError:
                    continue

        return ciphertext
    text = str(dig.plain_text.toPlainText())
    key  = str(dig.key.text())
    dig.cipher_text.setPlainText(str(encode(key, text)))
    

app = QtWidgets.QApplication([])
dig = uic.loadUi("task1.ui")
    
dig.rot13.clicked.connect(rot_13)
dig.trans.clicked.connect(Trans)

dig.show()
app.exec()
