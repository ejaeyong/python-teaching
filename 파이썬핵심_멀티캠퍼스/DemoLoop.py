# DemoLoop.py 
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break 
    print("Item:{0}".format(item))

print("---continue구문---")
for item in lst:
    if item % 2 == 0:
        continue
    print("Item:{0}".format(item))

#수열함수 
print( list(range(10)) )
print( list(range(1,11)) )
print( list(range(2000, 2022)) )

#리스트 컴프리헨션 
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print(result)
d = { 100:"apple", 200:"kiwi", 300:"orange" }
result = [v.upper() for v in d.values()]
print( result )

#필터링하는 함수
print("---필터링 함수---")
def getBiggerThan20(i):
    return i > 20

lst = [10, 25, 30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)