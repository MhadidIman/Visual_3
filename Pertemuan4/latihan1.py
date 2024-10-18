# QtGui QTCore QtWidgets
# CARA 1
from PyQt5 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QPushButton("MyButton")
window.show()
app.exec_()

# CARA 2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])
window = QPushButton("MyButton")
window.show()
app.exec_()

# CARA 3
from PyQt5 import QtWidgets as qtw

app = QApplication([])
window = QPushButton("MyButton")
window.show()
app.exec_()

# CARA 4 recommended
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])
window = QPushButton("MyButton")
window.show()
app.exec_()
