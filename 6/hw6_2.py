#**********************************************
# Name: 黄楷茵
# Class: 資管系三年級
# SID: s09490032
# Program Name: hw6_2.py
# Function:
# (1)宣告三個學生物件，並自行設定系所、年級、學號與姓
# (2)三個學生的成績設定如下(科目順序如上面)
# (ST1) 66、15、33、28、89、92
# (ST2) 78、25、63、58、73、46
# (ST3) 34、66、71、98、44、25
# (3)程式執行時可分別列印(輸出格式不限，請自行設計)
#  - 每位學生資料
#  - 依成績高低排序後的修課課名與成績
#  - 最高分科目與成績
#  - 最低分科目與成績
#  - 個人平均成績
# Homework: No. 6
# Date: 2023/1/4
#**********************************************

class Student:  #定義類別Student
    
    def __init__(self, department, grade, student_id, name, grades):  #initialization初始化
        self.department = department
        self.grade = grade
        self.student_id = student_id
        self.name = name
        self.grades = grades
        self.score = (("經濟成績：",self.grades[0]), ("會計成績：", self.grades[1]), ("統計成績：", self.grades[2]), ("管概成績：", self.grades[3]), ("計概成績：", self.grades[4]), ("程設成績：", self.grades[5]))      
        self.average = '{:.2f}'.format(sum(grades) / len(grades))
        self.string = '\0'
        self.highest_string = '\0'
        self.lowest_string = '\0'        
        self.scores = sorted(self.score, key = lambda x:x[1], reverse = True)  #排序成績高低
        self.score = self.scores
        
    def store_score(self):  #定義方法store_score
        self.score = list(self.score)  #原本的tuple形式轉存成list
        for i in self.score:  #使用for迴圈將list的資料依序排出
            self.string =self.string+ '\t'
            for j in i:
                self.string+=str(j)
            self.string+="\n"
        return self.string
    
    def find_highest_grade(self):  #定義方法find_highest_grade(找最高分)
        for j in self.score[0]:  #使用for迴圈進去已排序的list裡面抓第一個(最高分)資料出來
             self.highest_string += str(j)
        return self.highest_string
    
    def find_lowest_grade(self):  #定義方法find_lowest_grade(找最低分)
        for j in self.score[5]:  #使用for迴圈進去已排序的list裡面抓第最後一個(最低分)資料出來
             self.lowest_string += str(j)
        return self.lowest_string
    
    def __str__(self):  #物件導向的字串表達形式
        return f"系所：{self.department}\n" + \
               f"年級：{self.grade}\n" + \
               f"學號：{self.student_id}\n" + \
               f"姓名：{self.name}\n" + \
               f"{self.store_score()}" + \
               f"\t最低分：{self.find_lowest_grade()}\n" + \
               f"\t最高分：{self.find_highest_grade()}\n" + \
               f"\t平均成績：{self.average}\n"

st1 = Student('資管系', '大二', 'S10490100', '王捷', [66, 15, 33, 28, 89, 92])  #學生1的資料
st2 = Student('企管系', '大三', 'S09410100', '吳剛', [78, 25, 63, 58, 73, 46])  #學生2的資料
st3 = Student('財金系', '大四', 'S08440100', '琳菲', [34, 66, 71, 98, 44, 25])  #學生3的資料

print(st1)
print(st2)
print(st3)

input('Press any key to exit ...')






