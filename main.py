import sys
import VHDWriterUI

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = VHDWriterUI.Ui_MainWindow()

    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())