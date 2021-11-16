Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> strA = "python is very powerful"
>>> len(strA)
23
>>> strA[-8:]
'powerful'
>>> strB = """이번에는
다중 라인을 저쟁해 봅니다"""
>>> strB
'이번에는\n다중 라인을 저쟁해 봅니다'
>>> strB = """이번에는
다중 라인을 저쟁해 봅니다"""
>>> print(strB)
이번에는
다중 라인을 저쟁해 봅니다
>>> colors = ["red","blue","green"]
>>> len(colors)
3
>>> colors
['red', 'blue', 'green']
>>> colors.append("white")
>>> colors
['red', 'blue', 'green', 'white']
>>> colors.append("yellow")
>>> colors
['red', 'blue', 'green', 'white', 'yellow']
>>> colors. insert(1, "pink")
>>> colors
['red', 'pink', 'blue', 'green', 'white', 'yellow']
>>> colors
['red', 'pink', 'blue', 'green', 'white', 'yellow']
>>> colors.index("blue")
2
>>> colors.index("red")
0
>>> colors.count("red")
1
>>> colors += "red"
>>> colors
['red', 'pink', 'blue', 'green', 'white', 'yellow', 'r', 'e', 'd']
>>> colors.pop()
'd'
>>> colors.pop()
'e'
>>> colors.pop(1)
'pink'
>>> colors
['red', 'blue', 'green', 'white', 'yellow', 'r']
>>> 