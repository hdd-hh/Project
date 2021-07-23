# 1. 0~100 相加的和

a = 0
a1 = 0
while a1 <= 100:
    a += a1
    a1 += 1
print("1. a = ", a)

# 2. 打印 1~100 能被3整除的所有数的和
b = 0
while b <= 100:
    b += 1
    if b % 3 == 0:
        print("2. b = ", b)


# 3. 1~10 的奇数
for c in range(1, 11, 2):
    print("3. c = ", c)


# 4. 1~100 所有偶数和减去所有奇数和的值
d1 = 0
s = 0
d2 = 1
while d1 <= 100:
    s += d1
    d1 += 2
while d2 <= 100:
    s -= d2
    d2 += 2
print("4. 100以内偶数和减去奇数和等于 : ", s)


# 6. 判断输入的数能否被 3 和 5 同时整除

f = int(input("6. 输入一个整数 : "))
if f % 3 == 0 and f % 5 == 0:
    print("6. 这个数可以被 3 和 5 同时整除!")
else:
    print("6. 这个数不能被 3 和 5 同时整除!")


# 7. 输入一个数判断是否是 1~100 内的某个数  如是则打印

g1 = int(input("7. 输入一个整数 :"))
for g in range(1, 101):
    if g1 == g:
        print('7. ', g1, " 在 100 以内")
        break
else:
    print("7. 请输入 100 以内的数")


# 8. 输入三个整数，把他们由小到大输出
lst = []
for h in range(3):
    h1 = int(input("8. 列表排序，请输入一个整数:"))
    lst.append(h1)
lst.sort()
print(lst)


# 9. 按照 A B C D 等级划分输入的值

print('9. 输入你的成绩:')
score = int(input())
if score >= 90:
    print('您的成绩等级是:A')
elif score >= 78:
    print('您的成绩等级是:B')
elif score >= 60:
    print('您的成绩等级是:C')
else:
    print('您的成绩不合格!')


# 10. 将一个列表的数据复制到另一个列表中
print('10. 复制列表')
lst1 = ['abc', 'bcd', 'dcc']
lst2 = lst1[:]
print(lst2)


# 11. 输出 9 * 9 乘法口诀表
print('11. 9 * 9 乘法表')
for i1 in range(1, 10):
    for i2 in range(i1, 10):
        print(i1, "*", i2, "=", i1 * i2, end=' ')
    print()


# 12. 输入一行字符 分别统计出其中 英文 字母 空格 数字 和其他字符的个数
letter = 0
number = 0
space = 0
other = 0
j = input('请输入一个字符串:')
for j2 in j:
    if j2.isalpha():
        letter += 1
    elif j2.isdigit():
        number += 1
    elif j2.isspace():
        space += 1
    else:
        other += 1
print('12. 字母:', letter, '数字:', number, '空格:', space, '其他:', other)

# 13. 求 s = k + kk + kkk + ...+ k... n个数，n由键盘输入
print('计算 s = k + kk + kkk + ...+ k...')
k1 = int(input('13. 请输入一个小于 10 的正整数:'))
kf = int(input('13. 请输入循环次数:'))
s = 0
k2 = 0
for k3 in range(kf):
    k2 += k1
    k1 *= 10
    s += k2
print('13. ', s)

# 14. 打印菱形
l = '*'
sp = ' '
up = 4
down = 1
for l1 in range(1, 8):
    if l1 <= 4:
        vls1 = l * (2 * l1 - 1)
        vls2 = (up - l1) * sp
        ta = vls2 + vls1
        print(ta)
    else:
        vls3 = sp * (l1 - 4)
        vls4 = l * (7 - 2 * down)
        down += 1
        ta1 = vls3 + vls4
        print(ta1)
