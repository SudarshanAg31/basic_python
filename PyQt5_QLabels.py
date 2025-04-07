#PyQt5 QLabels
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my first GUI")
        self.setGeometry(650,400,500,700)
        self.setWindowIcon(QIcon("C:\\Users\\Lenovo\\OneDrive\\Pictures\\Camera Roll\\WIN_20250108_20_58_53_Pro.jpg"))
        label=QLabel("Hello",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:blue;"
                            "background-color:yellow;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")
        #label.setAlignment(Qt.AlignTop)#Vertically Top
        #label.setAlignment(Qt.AlignBottom)#Vertically Bottom
        #label.setAlignment(Qt.AlignVCenter)#Vertically Center
        
       #label.setAlignment(Qt.AlignRight)#Horizontally Right
       #label.setAlignment(Qt.AlignHCenter)#Horizontally center
       #label.setAlignment(Qt.AlignLeft)#Horizontally Left
        
       #label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)# Center & Top
       #label.setAlignment(Qt.AlignHCenter|Qt.AlignBottom)#Center & Bottom 
       #label.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)#center & center
        
        label.setAlignment(Qt.AlignCenter)#center & center
              
app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec_())