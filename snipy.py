# -*- coding: utf-8 -*-

import os
import sys
import pdb
from PySide import QtCore, QtGui
from PySide.QtUiTools import QUiLoader
from ui_snipy import Ui_MainWindow

class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # デバッグ
    #------------------------------------------------------------------------------
    # pdb.set_trace()

    # ウィンドウアクティブ
    #------------------------------------------------------------------------------
    # self.show()
    # self.activateWindow()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    sys.exit(app.exec_())
