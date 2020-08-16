# 文本进度条需求分析
# 采用字符串方式打印可以动态变化的文本进度条
# 进度条需要能在一行中逐渐变化

# TextProBarV1.py
import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("------执行结束------")


# 单行动态刷新
# 用后打印的字符覆盖之前的字符
import time
for i in range(101):
    print("\r{:3}%".format(i), end=" ") #\r表示光标回到行首，IDLE中屏蔽了\r功能
    time.sleep(0.1)


print("") # 换行

# 文本进度条完整效果
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter() # 获取精确时间计数值
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}-{}]{:.2f}s".format(c, a, b, dur), end=" ")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, "-"))
