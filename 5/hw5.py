#**********************************************
# Name: 黄楷茵
# Class: 資管系三年級
# SID: s09490032
# Program Name: hw5.py
# Function:
# 限定使用 yield 的方式來撰寫一個函式生成器(function generator)，
# 其功能為每一次執行時可以依序產生一個質數，此質數的產生範圍為正整數(從1至無限大)；
# 我們可以用課堂上教過的 send 指令重設起始點，但如果此起始點輸入為負數或零時會在螢幕上顯示錯誤訊息，
# 並視此次重設輸入為無效的變更，且維持原重設前的質數產生序列。
# Limitations:
# 請注意，hw5.py中只有此函式生成器的定義，無其它函式以外的指令，
# 質數的產生或重設等是在IDLE的shell介面上操作
# Homework: No. 5
# Date: 2022/12/18
#**********************************************

def findPrime():  #定義一個function generator名叫findPrime   
    val = 1  #設val初始值為1
    x = val  #變數x會等於val
    while True:  #進入無限迴圈
        if x is not None:
            if x > 0:
                val = x
                if is_prime(val):  #如果是質數            
                    x = yield val  #使用 yield 將val存回x            
                    if x is not None and isinstance(x, int):  #判斷x是否為空值，以及x是否為字串類型
                        if x <= 0:   #判斷x是否為負數                
                            x = yield '！！需輸入一個正整數，重設失敗！！'
                    elif type(x) == str:  #判斷x是否為字串
                        x = yield '！！需輸入一個正整數，重設失敗！！'  
                else:                    
                    val += 1
                    x = val
            else:
                x = yield '！！需輸入一個正整數，重設失敗！！'
        else:
            val+= 1  #產生的值數+1，之後會再進入while迴圈裡面判斷
            x = val

def is_prime(n):  #function generator名叫is_prime，用來判斷是否為質數
    if n >= 2:
        for i in range(2, n):  #迴圈從 2 到 n-1 檢查 n 是否可被任何數整除       
            if n % i == 0:  #如果可以整除
                return False  #則 n 不是質數      
        return True  #所有小於 n 的數仍然無法整除 n，則 n 是質數
    else:       
        return False




        


