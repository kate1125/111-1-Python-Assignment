#**********************************************
# Name: 黄楷茵
# Class: 資管系三年級
# SID: s09490032
# Program Name: hw6_1.py
# Function:
# (1)圓形類別:需記錄半徑，並宣告面積與周長計算的方法。
# 宣告二個圓形物件: (一)半徑: 5cm，(二) 半徑: 12.5cm，並分別計算與顯示其面積與周長。
# (2)長方形類別:需記錄長和寬，並宣告面積與周長計算的方法。
# 宣告二個長方形物件: (一)長: 6cm、寬: 100cm，(二)長: 13cm、寬: 62cm，並分別計算與顯示其面積與周長。
# (3)梯形類別:需記錄上底、下底與高，並宣告面積計算的方法。
# 宣告二個梯形物件: (一)上底: 15cm、下底: 20cm、高: 6cm，(二)上底: 8cm、下底: 60cm、高: 18cm，並分別計算與顯示其面積。
# (4)三角形類別:需記錄底與高，並宣告面積計算的方法。
# 宣告二個三角形形物件: (一)底: 13cm、高: 8cm，(二)底: 21.5cm、高: 18cm，並分別計算與顯示其面積。
# Homework: No. 6
# Date: 2023/1/1
#**********************************************

import math

#(1)
class Circle():  #定義類別Circle
    def __init__(self, r):  #定義方法，輸入參數為self與r
        self.r = r  #將r儲存到物件變數self.r
    def area(self):  #定義方法area
        return math.pi * self.r ** 2  #回傳圓面積公式
    def perimeter(self):  #定義方法perimeter
        return 2 * math.pi * self.r  #回傳圓周長公式

r1 = Circle(5)
r2 = Circle(12.5)

print('圖形物件一'"\n                ", '面積：', round(r1.area(), 2), '平方公分')
print("                ", '周長：', round(r1.perimeter(), 2), '平方公分')
print('圖形物件二'"\n                ", '面積：', round(r2.area(), 2), '平方公分')
print("                ", '周長：', round(r2.perimeter(), 2), '平方公分')

#(2)
class Rectangle():  #定義類別Rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

R1 = Rectangle(6, 100)
R2 = Rectangle(13, 62)

print('\n長方形物件一'"\n                ", '面積：', '{:.2f}'.format(R1.area()), '平方公分')
print("                ", '周長：', '{:.2f}'.format(R1.perimeter()), '平方公分')
print('長方形物件二'"\n                ", '面積：', '{:.2f}'.format(R2.area()), '平方公分')
print("                ", '周長：', '{:.2f}'.format(R2.perimeter()), '平方公分')

#(3)
class Trapezoid():  #定義類別Trapezoid
    def __init__(self, top_base, bottom_base, height):
        self.top_base = top_base
        self.bottom_base = bottom_base
        self.height = height
    def s(self):
        return (self.top_base + self.bottom_base) * self.height / 2

Tra1 = Trapezoid(15, 20, 6)
Tra2 = Trapezoid(8, 60, 18)

print('\n梯形物件一'"\n                ", '面積：', '{:.2f}'.format(Tra1.s()), '平方公分')
print('梯形物件二'"\n                ", '面積：', '{:.2f}'.format(Tra2.s()), '平方公分')

#(4)
class Triangle():  #定義類別Triangle
    def __init__(self, bottom, height):
        self.bottom = bottom
        self.height = height
    def s(self):
        return self.bottom * self.height / 2
    
Tri1 = Triangle(13, 8)
Tri2 = Triangle(21.5, 18)

print('\n三角形物件一'"\n                ", '面積：', '{:.2f}'.format(Tri1.s()), '平方公分')
print('三角形物件二'"\n                ", '面積：', '{:.2f}'.format(Tri2.s()), '平方公分')

input('\nPress any key to exit ...')

