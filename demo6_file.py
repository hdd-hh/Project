# 文件操作步骤
"""
1. 打开文件                  open('文件名')
2. 读、写文件
    读取文件内容到内存中       read()
    写入内容到文件中          write()
3. 关闭文件                 close()
"""


# 读取文件 a.txt 中的内容并输出
"""
f = open('a.txt')
contents = f.read()
print(contents)
f.close()
"""

f = open('a.txt')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()
