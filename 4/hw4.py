#**********************************************
# Name: 黄楷茵
# Class: 資管系三年級
# SID: s09490032
# Program Name: hw4.py
# Function:
# (已知執行Python模組中的 this.py，可以在螢幕上顯示出由Tim Peters所寫下關於Python的精神指標與哲學 - ”The Zen of Python”。this.py這程式一開始利用一個字串儲存 ”The Zen of Python” 原文加密後的結果，後續利用字典(dict)的處理技巧將原文解密之後顯示在螢幕上。)
# (1)顯示解密的原文。
# (2)將上述(1)中的原文解密結果再度加密回去；並與原始解密前的字串作資料比對，如果任何一個字、一個標點符號或任何一個空格都沒有錯誤與遺失的話，則在螢幕上顯示出 ” 加密內容經比對後正確無誤！” 等字樣。(※若再度加密後的比對結果不正確則表示您的程式有誤，請務必修正。)
# (3)計算並顯示執行(1)解密之後原文中的字元個數，此處包含標點符號與空白。
# (4)將執行(1)解密之後的原文做文字處理，包含字元分類與計算相同字元出現的次數，並將結果顯示列印出來。
# Homework: No. 4
# Date: 2022/12/4
#**********************************************

#1

print('>> (a)小題 : 顯示解密的原文內容\n')

s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}

for c in (65, 97): #ASCII碼對應字元 A: 65, a:97 
    for i in range(26): #26個字元  
        d[chr(i+c)] = chr((i+13) % 26 + c) #透過轉換讓A = N

a = ("".join([d.get(c, c) for c in s])) #將結果先預存成串列
print(a)

#2

print("\n>> (b)小題 : 比對'再加密之後的字串'與'解密前的字串'內容是否相同無誤")

b = list(s) #將原本str(s)存成字串
c = list("".join([d.get(j, j) for j in a])) #變數c為再加密後的字串

if (b==c) : #如果"str(s)的字串" = "再加密後的字串"
    print('\n比對結果 : 加密內容經比對後正確無誤！') #印出結果(正確)
else:    
    print('\n比對結果 : 加密內容經比對後錯誤！') #印出結果(錯誤)

#3

print('\n>> (c)小題 : 計算並顯示執行#1解密之後原文中的字元個數(包含標點符號與空白)')
print('\n原文解密後的字元個數 ： ', len(a)) #計算並顯示執行#1解密之後原文中的字元個數

#4

print('\n>> (d)小題 : 將(a)解密之後的原文做(1)字元分類與(2)計算相同字元出現的次數')
print('\n字元分類與出現個數 ：\n' )
print("         字元 \t： 出現次數\n        ====================")

from collections import Counter #插入collections套件

dic = {w:a.count(w) for w in set(a) if w != '，' and w != '。' } #使用for迴圈，與函式set(a)取出變數a中的每個文字轉換集合，集合會自動去除重複的文字

num = sorted(dic) #無序的鍵列表中建立一個新的、有序的字典

for i in sorted(dic.keys()): #通過從字典中選擇每個條目，對該排序列表重複進行排序
    print("         ", repr(i), "\t：", dic[i]) #列印出結果

print()
input('Press any key to exit ....') #結束程式的執行











    
 


