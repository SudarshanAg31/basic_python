#PyQt5 introduction
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my first GUI")
        self.setGeometry(550,300,800,600)# x,y,width,height
        self.setWindowIcon(QIcon("C:\\Users\\Lenovo\\OneDrive\\Pictures\\Camera Roll\\WIN_20250108_20_58_53_Pro.jpg"))
app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec_())        

#PyQt5:- it is an pakeage and QtWidgets is module 

#QMainWindow :-QMainWindow is a parent class use for create main window 
# so,we create MainWindow class to call parent to access QMainWindow

#QApplication:-QApplication is use to create aap 

#window.show():- show the window

#sys.exit(aap.exec_()): Run the code and handle closing  

#app.exec_():It keeps the application running until the user closes the window