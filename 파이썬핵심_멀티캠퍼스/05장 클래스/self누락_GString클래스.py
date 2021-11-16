#전역변수
str = "Not Class Member"
#클래스 정의
class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):#this 도 가능함.
        #버그 발생~~ 오류수정 완료
        print(self.str)

g = GString()
g.set("First Message")
g.print()
