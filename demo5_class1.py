"""
class Students():
    name = ""
    grade = 0

    def study(self, course):
        print("学生 {}, 目前 {} 年级, 正在学习 {}".format(self.name, self.grade, course))


s = Students()
s.name = "张三"
s.grade = 5
s.study('语文课')
"""


# 通过构造方法去实现
class Students():
    # 构造方法
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, course):
        print("该学生是 : {}, 学生 {}, 目前 {} 年级, 正在学习 {}".format(self, self.name, self.grade, course))


s = Students("张三", "5年级")
s.study("语文课")

print('='*20)
s = Students("李四", "5年级")
s.study("数学课")
