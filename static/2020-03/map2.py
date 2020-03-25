import sys
from PySide2 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel("Hello, World!")
label.show()

sys.exit(app.exec_())
