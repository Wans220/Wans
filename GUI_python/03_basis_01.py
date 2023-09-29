import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        # 상태바 만들기
        self.statusBar().showMessage('Ready')
        
        # 버튼 툴팁 셋팅
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidgets</b> widget')
        
        # 버튼 셋팅
        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        # 창이 열리는 셋팅
        self.setWindowTitle('My First Application') # set widgets' title
        self.setWindowIcon(QIcon('web.png'))        # add icon to the widget's title
        self.move(300, 300)                         # setting location of widgets  
        self.resize(400, 200)                       # setting size of widgets
        self.show()                                 # command with open widgets
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
