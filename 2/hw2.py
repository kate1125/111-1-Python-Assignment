#**********************************************
# Name: 黄楷茵
# Class: 資管系三年級
# SID: s09490032
# Program Name: hw2.py
# Function: 
# (1) 產生一個內含apple, pineapple, banana, grape, orange, watermelon的串列物件fruits，並將結果輸出在螢幕上。
# (2) 利用 + 和 * 指令與fruits物件，產生內含apple, pineapple, banana, pineapple, banana, grape, banana, grape, orange, grape, orange, watermelon的串列物件rep1_fruits，並將結果輸出在螢幕上。
# (3) 隨意使用append()、extend()或insert()其中任何方法，並利用 * 指令與fruits物件，產生內含apple, pineapple, banana, pineapple, banana, grape, banana, grape, orange, grape, orange, watermelon (以上順序不可改變) 的串列物件rep2_fruits，並將以上結果依序輸出在螢幕上。(note: extend()方法如何使用請自行上網尋找)
# (4) 利用del指令移除rep1_fruits物件內之所有banana，接著再使用remove()指令移除所有grape，並將以上結果依序輸出在螢幕上。
# (5) 利用pop()指令移除rep2_fruits物件內最後一項watermelon，接著繼續使用pop()指令移除所有orange，並將以上結果依序輸出在螢幕上。
# (6) 將rep2_fruits串列物件轉換成rep3_fruits元祖(tuple)容器物件。再利用count()指令計算出有多少個pineapple在rep3_fruits中，再利用index()指令找出pineapple物件第一次出現所在位置的指標索引值(index)。分別檢查banana與orange是否出現在rep3_fruits中，並將以上結果依序輸出在螢幕上。
# Homework: No.2
# Limitations: 
# (1)本次作業限定使用已教過的Python指令語法（ch2, ch3），不可以用 if，for 等指令
# Date: 2022/11/13
#**********************************************
#1
fruits = ['apple', 'pineapple', 'banana', 'grape', 'orange', 'watermelon'] #設定變數fruits，產生一個串列物件
print('(1) Answer：\n\nfruits =', fruits)

#2
fruits = list(('apple', 'pineapple', 'banana', 'grape', 'orange', 'watermelon')) #使用函式list產生串列
fruits_ = ['pineapple']
fruits__ = ['banana', 'grape']*2 #使用*指令新增元素
fruits___ = ['orange']
rep1_fruits = fruits[0:3]+fruits_+fruits__+fruits___+fruits[3:] #利用+以及list[:]產生串列物件rep1_fruits
print('\n(2) Answer：\n\nrep1_fruits =', rep1_fruits)

#3
fruits = list(('apple', 'pineapple', 'banana', 'grape', 'orange', 'watermelon'))
fruits.insert(3, 'pineapple') #使用insert()插入元素
fruits.insert(4, 'banana')
fruits.insert(5, 'grape')
fruits.insert(6, 'banana')
fruits.insert(7, 'grape')
fruits.insert(8, 'orange')
print('\n(3) Answer：\n\nrep2_fruits =', fruits)

#4
print('\n(4) Answer：\n\nOriginal list：\nrep1_fruits =', rep1_fruits)

del rep1_fruits[2] #利用del指令移除物件裡的'banana' (因為[依序]移除，所以會做三次)
print("\nDelete the first 'banana'：\nrep1_fruits =", rep1_fruits)

del rep1_fruits[3] #利用del指令移除物件裡的'banana'
print("\nDelete the second 'banana'：\nrep1_fruits =", rep1_fruits)

del rep1_fruits[4] #利用del指令移除物件裡的'banana'
print("\nDelete the third 'banana'：\nrep1_fruits =", rep1_fruits)

rep1_fruits.remove('grape') #利用remove()指令移除物件裡的'grape' (因為[依序]移除，所以會做三次)
print("\nRemove the first 'grape' from the list：\nrep1_fruits =", rep1_fruits)

rep1_fruits.remove('grape') #利用remove()指令移除物件裡的'grape'
print("\nRemove the second 'grape' from the list：\nrep1_fruits =", rep1_fruits)

rep1_fruits.remove('grape') #利用remove()指令移除物件裡的'grape'
print("\nRemove the third 'grape' from the list：\nrep1_fruits =", rep1_fruits)

#5
print('\n(5) Answer：\n\nOriginal list：\nrep2_fruits =', fruits)

fruits.pop() #利用pop()指令移除rep2_fruits物件內最後一項'watermelon'
print("\nPop the last object named 'watermelon' off the list：\nrep2_fruits =", fruits)

fruits.pop() #使用pop()指令移除'orange' (因為[依序]移除，所以會根據不同位置做兩次)
print("\nPop the last object named 'orange' off the list ：\nrep2_fruits =", fruits)

fruits.pop(-2) #使用pop()指令移除'orange'
print("\nPop the object named 'orange' off the list：\nrep2_fruits =", fruits)

#6
rep3_fruits = tuple(fruits) #將rep2_fruits串列物件轉換成rep3_fruits元祖(tuple)容器物件
print('\n(6) Answer：\n\nrep3_fruits =', rep3_fruits)
print("\nThere are", rep3_fruits.count('pineapple'), "objects named 'pineapple' in the rep3_fruits.") #利用count()指令計算出有多少個pineapple在rep3_fruits中
print("\nThe index of the first object named 'pineapple' in the rep3_fruits is", rep3_fruits.index('pineapple'), ".") #利用index()指令找出pineapple物件第一次出現所在位置的指標索引值(index)

set = rep3_fruits
print("\nIs the object named 'banana' in the rep3_fruits?：", 'banana' in set) #檢查'banana'是否出現在rep3_fruits中，並印出結果
print("\nIs the object named 'orange' in the rep3_fruits?：", 'orange' in set) #檢查'orange'是否出現在rep3_fruits中，並印出結果

print()
input('Press any key to exit....')
