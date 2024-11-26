import math
import sys


def format01():
    str = math.pi
    print(str)  # 3.14159265359'
    str = format(math.pi, ".18f")  # PI 取小數點18位
    print(str)  # 3.141592653589793116
    str = "PI = {0.pi}".format(math)  # 第0個對應後面第0個參數
    print(str)  #'PI = 3.14159265359'
    str = "My platform is {pc.platform}".format(pc=sys)  # 以符號 pc 對應 sys
    print(str)  #'My platform is win32'
    str = "My platform is {0.platform}. PI = {1.pi}.".format(sys, math)
    print(str)
    #'My platform is win32. PI = 3.14159265359.'
    str = "element of index 1 is {0[1]}".format([20, 10, 5])  # 第0個對應後面第0個參數
    print(str)  #'element of index 1 is 10'
    str = "My name is {person[name]}".format(person={"name": "Justin", "age": 35})
    print(str)


format01()
