#%%
import sys
from PyQt4 import QtGui
# %%
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1000,700)
        self.setWindowTitle('LiuHongLFPIV')
        self.setWindowIcon(QtGui.QIcon('Liu.ico'))
        self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

# %%
