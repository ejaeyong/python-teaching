# web2.py
#웹서버에 요청 
import urllib.request
#크롤링 
from bs4 import BeautifulSoup

'''
https://bank.shinhan.com/index.jsp#020501010100

<strong id="wq_uuid_4829" class="w2textbox ">기준일시(회차)</strong>

날짜<span id="wq_uuid_4830" class="w2textbox time">2021.11.18 18:00:11 (179회차)</span>

구분
<td blockselect="false" id="grd_list_1_cell_0_0" inputtype="text" headers="grd_list_1_column1" colindex="0" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_0_ focusedTr" style="text-align: center;" col_id="통화CODE_display" scope="row" tdindex="0" or_bgcolor="">
    <nobr class="w2grid_input w2grid_input_readonly">미국 달러
    </nobr>
</td>
통화표시<td blockselect="false" id="grd_list_1_cell_0_1" inputtype="user" headers="grd_list_1_column2" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_1_ focusedTr" style="text-align: center;" col_id="통화CODE" tdindex="1" or_wd="70" or_bgcolor=""><nobr><a href="javascript:shbObj.fncGoPage('USD')"><p class="icon_sign_usd">USD</p></a></nobr></td>
매매기준율<td blockselect="false" id="grd_list_1_cell_0_2" inputtype="text" textalign="right" headers="grd_list_1_column3" colindex="2" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_2_ focusedTr" style="text-align: right;" col_id="매매기준환율_display" tdindex="2" or_wd="70" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1,181.00</nobr></td>
송금(받으실때)<td blockselect="false" headers="grd_list_1_column7 grd_list_1_column4" id="grd_list_1_cell_0_3" inputtype="text" textalign="right" colindex="3" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_3_ focusedTr" style="text-align: right;" col_id="전신환매입환율_display" tdindex="3" or_wd="70" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1,169.70</nobr></td>
송금(보내실때)<td blockselect="false" headers="grd_list_1_column8 grd_list_1_column4" id="grd_list_1_cell_0_4" inputtype="text" textalign="right" colindex="4" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_4_" style="text-align: right;" col_id="전신환매도환율_display" tdindex="4" or_wd="55" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1,192.30</nobr></td>
현찰(파실때)<td blockselect="false" headers="grd_list_1_column9 grd_list_1_column5" id="grd_list_1_cell_0_5" inputtype="text" textalign="right" colindex="5" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_5_ focusedTr" style="text-align: right;" col_id="지폐매입환율_display" tdindex="5" or_wd="55" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1,160.34</nobr></td>
현찰(파실때스프레드)<td blockselect="false" headers="grd_list_1_column10 grd_list_1_column5" id="grd_list_1_cell_0_6" inputtype="text" displaymode="label" textalign="right" datatype="number" displayformat="#,###.00" colindex="6" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_6_ focusedTr" style="text-align: right;" col_id="지폐매입스프레드_display" tdindex="6" or_wd="70" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1.75</nobr></td>
현찰(사실때)<td blockselect="false" headers="grd_list_1_column11 grd_list_1_column5" id="grd_list_1_cell_0_7" style="text-align: right; height: 20px;" inputtype="text" displaymode="label" textalign="right" colindex="7" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_7_ focusedTr" col_id="지폐매도환율_display" tdindex="7" or_wd="70" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1,201.66</nobr></td>
현찰(사실때스프레드)<td blockselect="false" headers="grd_list_1_column12 grd_list_1_column5" id="grd_list_1_cell_0_8" style="text-align: right; height: 20px;" inputtype="text" displaymode="label" textalign="right" datatype="number" displayformatter="" displayformat="#,###.00" colindex="8" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_8_ focusedTr" col_id="지폐매도스프레드_display" tdindex="8" or_wd="70" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1.75</nobr></td>
대미환산율<td blockselect="false" id="grd_list_1_cell_0_9" inputtype="text" displaymode="label" textalign="right" headers="grd_list_1_column6" colindex="9" role="gridcell" class="w2grid_input_table gridBodyDefault gridBodyDefault_data grd_list_1_columnstyle_9_ focusedTr" style="text-align: right;" col_id="대미환산환율_display" tdindex="9" or_wd="70" or_bgcolor=""><nobr class="w2grid_input w2grid_input_readonly">1.0000</nobr></td>
'''


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
