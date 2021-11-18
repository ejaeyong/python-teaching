# DemoForm2.py
# DemoForm2.ui(화면단), DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#화면을 로딩
form_class = uic.loadUiType(r"D:\교육\교육Git\파이썬핵심_멀티캠퍼스\DemoForm2.ui")[0]

#폼클래스(윈도우)를 정의(수정 QMainWindow )
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.label.setText("첫번째 데모")
    def firstClick(self):
        self.label.setText("첫번째~~")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~")

#진입점을 체크
# if __name__ == "__main__":
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show() 
app.exec_()