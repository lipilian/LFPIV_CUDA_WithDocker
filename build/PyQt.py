#%%
import sys
from PyQt4 import QtGui, QtCore
import OpenGL
from settings import Settings
import os

# %%
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1000,700)
        self.setWindowTitle('LiuHongLFPIV')
        self.setWindowIcon(QtGui.QIcon('Liu.ico'))

        # main manual 
        extractAction = QtGui.QAction("Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave The App")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.close_application()

    
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(500,500)

        extractAction = QtGui.QAction('Tool', self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar('Extraction')
        self.toolbar.addAction(extractAction)

        self.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!', 
                                            "Did you save the setting ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if choice == QtGui.QMessageBox.Yes:
            print("program closed by user")
            sys.exit()
        else:
            pass

# %%

def run():
    app = QtGui.QApplication(sys.argv)
    qt_settings = QtCore.QSettings(QtCore.QSettings.IniFormat,
                            QtCore.QSettings.UserScope,
                            'University of Illinois at Urbana-Champaign',
                            'LFDisplay-CUDA')
    
    cwd = os.path.dirname(os.path.realpath(__file__)) # ? os.getcwd() if use the global document path 
    outputPath = os.path.join(cwd, 'output')
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    inputPath = os.path.join(cwd, 'input')
    if not os.path.exists(inputPath):
        os.makedirs(inputPath)
    
    GUI = Window()
    sys.exit(app.exec_())

    
if __name__ == '__main__':
    run()

# %%
