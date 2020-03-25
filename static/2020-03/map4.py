import sys
from PySide2 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        button = QtWidgets.QPushButton("Hello, World!")
        label = QtWidgets.QLabel("-empty-")

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button)
        layout.addWidget(label)

        window_content = QtWidgets.QWidget()
        window_content.setLayout(layout)
        self.setCentralWidget(window_content)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
