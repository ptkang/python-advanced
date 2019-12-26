# 500G的文件，且比较特殊只有一行
# f = open()
# for line in f:
# f.readlines()
# 以上几个两个方法都放不到内存里面
# f.read(4096) 可以按大小读取

def my_readlines(f, newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096 * 10)
        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk

with open('input.txt') as f:
    for line in my_readlines(f, '{|}'):
        print(line)