# by julian: 2026
import sys
import os
from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)
main_ui_file = "/Users/julianjurista/Visual Studio Code/Software Dev 2026/taskmanager.ui"
add_task_file = "/Users/julianjurista/Visual Studio Code/Software Dev 2026/addTask.ui"
info_file = "/Users/julianjurista/Visual Studio Code/Software Dev 2026/info.ui"
win = uic.loadUi(main_ui_file)
win2 = uic.loadUi(add_task_file)
win3 = uic.loadUi(info_file)

# functions


def go_button_clicked():
    win2.show()

def info_button_clicked():
    win3.show()

def info_ok_button_clicked():
    win3.close()

def win2_go_button_clicked():
    win2.close()

def win2_add_task_button_clicked():
    win2.close()


 
#make a dictionary of the entered details in add task
# do that by making a copy of taskmanager.ui, then making the changing to the xml, extract the details from there and make the dictionary
#make the ui look nice

# Connect Buttons
win.pushButtonAddTask.clicked.connect(go_button_clicked)
win2.pushButtonCancel.clicked.connect(win2_go_button_clicked)
win2.pushButtonAdd.clicked.connect(win2_add_task_button_clicked)
win.pushButtonInfo.clicked.connect(info_button_clicked)
win3.pushButtonInfoOK.clicked.connect(info_ok_button_clicked)

# Show the window
win.showFullScreen()
sys.exit(app.exec())