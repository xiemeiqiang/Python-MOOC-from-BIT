# 自动轨迹绘制
# 需求：根据脚本绘制图形
# 基本思路
# 步骤1：定义数据文件格式（接口）
# 步骤2：编写程序，根据文件接口解析参数绘制图形
# 步骤3：编制数据文件
# 数据接口定义
# <行进距离>,<转向判断（0：左转，1：右转）>,<转向角度>,<RGB三个通道颜色（0-1之间的浮点数）>例如：300，1,144,0,1,0,

# AutoTraceDraw.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
# 数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    if line !="":           #eval内参数为空时报错EOF，需加if判断
        datals.append(list(map(eval, line.split(","))))
    # map函数的作用是将第一个参数的功能，作用于第二个参数的每一个元素，第一个参数就是函数的名字
f.close()
# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
