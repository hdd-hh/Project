# 异常和错误:
"""
try:
    可能出现错误的代码
except Exception e:
    print(e)
"""
# 使用try ... except Exception e: ...

"""
f = None
try:
    f = open('c.txt')
    for x in f.readline():
        print(x, end='')
except Exception as e:
    print(e)
if f:
    f.close()
"""

# 无论结果如何，部分代码都希望被执行到, 可使用  try ... except ... finally ,把需要执行的代码放在finally语句中
f = None
try:
    f = open('a.txt')
    for x in f.readline():
        #raise('抛出异常')
        print(x, end='')
except Exception as e:
    print(e)

finally:
    print("-------")
    if f:
        f.close()
