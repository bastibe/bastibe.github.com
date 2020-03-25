import sys
from PySide2 import QtCore
from PySide2 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        button = QtWidgets.QPushButton("Hello, World!")
        self.label = QtWidgets.QLabel("-empty-")
        button.clicked.connect(self.change_button_content)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.label)

        window_content = QtWidgets.QWidget()
        window_content.setLayout(layout)
        self.setCentralWidget(window_content)

    @QtCore.Slot()
    def change_button_content(self):
        self.label.setText("no longer empty")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
