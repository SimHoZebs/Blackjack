# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 02:14:10 2019

@author: simho

QtWidgets.QVBoxLayout() makes window box
"""

from PySide2 import QtWidgets
import sys

app = QtWidgets.QApplication.instance()
if app is None:
    app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout()
layout.addWidget(QtWidgets.QLabel("<font color=red size=40>Hello World!</font>"))
layout.addWidget(QtWidgets.QPushButton("Top"))
layout.addWidget(QtWidgets.QPushButton("Bottom"))
window.setLayout(layout)
window.show()
app.exec_()