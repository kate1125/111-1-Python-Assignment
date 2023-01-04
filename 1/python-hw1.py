#**********************************************
# Name: 黄楷茵
# Class: 資管系三年級
# SID: s09490032
# Program Name: hw1.py
# Function:
#                   (1) 在使用者操作登入時，系統畫面會明確提示要求輸入【身分證號碼】或【手機號碼】其中一個選項。
#                   (2) 在使用者完成輸入後，系統會判讀並驗證客戶輸入的是身分證號碼還是手機號碼的格式是否正確。
#                   (3) 完成上述工作之後，程式只會輸出【身分證號碼有效格式】、【手機號碼有效格式】或【登入錯誤 – 無效格式】其中一個結果於螢幕上。
# Homework: No.1
# Limitations:
#                   (1)僅限於負責驗證輸入格式是否正確，並不涉及客戶登入的資料內容與後端資料庫內的個資設定是否相同的認證問題。
# Date: 2022/10/22
#**********************************************

n = input('請輸入個人的 [身分證號碼] 或 [手機號碼]：')   #設定變數n，加上提示字語讓使用者輸入
length = list(n)    #新增length變數，將身分證字號轉換成串列存入

if length[0].istitle() and len(length) == 10 and (length[1] == '1' or length[1] == '2'):     #如果變數length的第一個位置是英文字母大寫，長度為10，第二個位置的值是1(男)或是2(女)
    print('【身分證號碼有效格式】')    #輸出【身分證號碼有效格式】
elif len(length) == 10 and length[0] == '0' and length[1] == '9':     #如果length的長度等於10，第一個位置的值0，第二個位置的值是9
    print('【手機號碼有效格式】')     #輸出【手機號碼有效格式】
else:   #以上條件都不符合
    print('【登入錯誤 – 無效格式】')   #輸出【登入錯誤 – 無效格式】
    
print()
input('Press any key to exit ...')      #結束程式的執行



    
