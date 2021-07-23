# 函数

# 1. 定义函数
"""
def 函数名(参数列表):
    定义的代码块
"""


# 两个数相加
def add(x, y):
    z = x + y
    return z


def add1(x, y):
    return x + y


def calc(x, y):
    sum1 = x + y
    sum2 = x * y
    return sum1, sum2


print(add(1, 2))
print(add1(3, 5))
print(calc(2, 4))


# 关键字参数
def student_lesson(grade, subject):
    z = '{}期同学上{}课'.format(grade, subject)
    return z


# 位置参数调用
print(student_lesson(24, 'python'))


# 关键字参数调用
print(student_lesson(subject='python', grade=24))


# 默认参数
def study_language(name, language='python'):
    info = ('{}要学习{}语言'.format(name, language))
    return info


print(study_language('张三', 'java'))
print('默认python', study_language('李四'))


# 可变化参数
# 1. 列表形式的可变化参数
def show_info(*args):
    print(*args)


tp = ('1', '2', '3')
lst = ['1', '2', '3']
show_info('hello')
show_info('hello', 'world')
show_info(tp)
show_info(lst)


# 2. 字典形式的可变化参数
def show_info1(**kwargs):
    print(kwargs)


dt = {'lesson_name': 'python', 'grade': '5年级', 'a': 'a'}
show_info1(lesson_name='python')
show_info1(lesson_name='python', grade='5年级')
show_info1(**dt)


# 可变化参数结合起来使用
def show_info2(*args, **kwargs):
    print(*args)
    print(**kwargs)


def show_info3(a, b, *args, **kwargs):
    print(*args)
    print(**kwargs)
