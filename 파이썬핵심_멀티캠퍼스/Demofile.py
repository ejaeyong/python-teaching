# DemoFile.py 

#한글로 쓰기와 읽기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째\n세번째\n")
f.close()

print( f.closed )

#읽기 
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
print("---read()---")
print( f.read() )
print("---readline()---")
print( f.tell() )
f.seek(0)
print( f.readline() )
print( f.readline() )
print("---readlines()---")
f.seek(0)
print( f.readlines() )