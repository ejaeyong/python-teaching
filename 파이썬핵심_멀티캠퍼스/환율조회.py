# web2.py
#웹서버에 요청 
import urllib.request
#크롤링 
from bs4 import BeautifulSoup

#파일로 저장(파일이 없으면 생성, 있으면 맨뒤로 가서 첨부)
# f = open(r"D:\교육\교육Git\파이썬핵심_멀티캠퍼스\환율정보.txt", "rw", encoding="utf-8")

url = "https://bank.shinhan.com/index.jsp#020501010100"
#페이지 처리 
data = urllib.request.urlopen(url)
#검색이 용이한 객체 
soup = BeautifulSoup(data, "html.parser")
nations = soup.find_all("td", class_="col_id")

# for nation in nations:
#     title = nation.find("a").text 
#     print( title.strip() )
#     f.write(title.strip() + "\n")

print(nations[0])

#수열함수로 1부터 5까지 생성 
# for i in range(1,6):
#     url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
#     #페이지 처리 
#     data = urllib.request.urlopen(url)
#     #검색이 용이한 객체 
#     soup = BeautifulSoup(data, "html.parser")
#     cartoons = soup.find_all("td", class_="title")

#     for item in cartoons:
#         title = item.find("a").text 
#         print( title.strip() )
#         f.write(title.strip() + "\n")

# f.close()
# print("저장 완료~~")
