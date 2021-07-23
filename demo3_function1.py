# 多个数不定相加的函数

def plus(a, b, *args):
    s = 0
    if args:  # 如果元组不为空
        for x in args:
            s += x
    return s + a + b


print(plus(1, 2))
