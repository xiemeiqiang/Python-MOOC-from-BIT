# 基本思路
# 步骤1：绘制单个数字对应的数码管
# 步骤2：获得一串数字，绘制对应的数码管
# 步骤3：获得当前系统时间，绘制对应的数码管
# 美化
# 增加七段数码管之间线条间隔
# 增加年月日的标记，并颜色不同

import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    # 三目运算符
    # 对于条件表达式  b ? x : y ，
    # 先计算条件b，然后进行判断。
    # 如果b的值为true，计算x的值，运算结果为x的值；否则，计算y的值，运算结果为y的值。
    # 一个条件表达式绝不会既计算x，又计算y。条件运算符是右结合的，也就是说，从右向左分组计算。
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write("年",font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月", font=("Arial", 18, "normal"))
        elif i == '+':
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()
