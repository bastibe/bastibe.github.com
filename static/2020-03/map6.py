import sys
import json
from PySide2 import QtCore
from PySide2 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        map_data = self.load_map_data()
        for country, polygon in map_data.items():
            print(country, len(polygon))

        layout = QtWidgets.QHBoxLayout()

        window_content = QtWidgets.QWidget()
        window_content.setLayout(layout)
        self.setCentralWidget(window_content)

    def load_map_data(self):
        with open('countries_110m.json') as f:
            data = json.load(f)

        return data

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
