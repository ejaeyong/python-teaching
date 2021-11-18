# DemoForm2.py
# DemoForm2.ui(화면단), DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹서버에 요청 
import urllib.request
#크롤링 
from bs4 import BeautifulSoup

#화면을 로딩
form_class = uic.loadUiType(r"D:\교육\교육Git\파이썬핵심_멀티캠퍼스\DemoForm2.ui")[0]

#폼클래스(윈도우)를 정의(수정 QMainWindow )
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.label.setText("첫번째 데모")
    def firstClick(self):
        #파일로 저장
        # f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        # f=open(r"D:\교육\교육Git\파이썬핵심_멀티캠퍼스\webtoon.txt", "wt", encoding="utf-8")
        f=open(r"D:\교육\교육Git\파이썬핵심_멀티캠퍼스\webtoon.txt", "a+", encoding="utf-8")#append read write
        #수열함수로 1부터 5까지 생성 
        for i in range(1,6):
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            #페이지 처리 
            data = urllib.request.urlopen(url)
            #검색이 용이한 객체 
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")

            for item in cartoons:
                title = item.find("a").text 
                print( title.strip() )
                f.write(title.strip() + "\n")
        f.close()
        self.label.setText("웹툰 크롤링 종료~~")
        
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