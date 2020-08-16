# 第1问：计算1‰的力量
# daydayupQ1.py
dayup = pow(1.001, 365)
daydown = pow(0.999, 365)
print("第1问：1‰的力量")
print("向上：{:.2f}，向下：{:.2f}\n".format(dayup, daydown))

# 第2问：5‰和1%的力量
# daydayupQ2.py
# 修改dayfactor的值为0.005和0.1
dayfactor = 0.005
dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)
print("第2问：5‰和1%的力量：")
print("向上：{:.2f}，向下：{:.2f}\n".format(dayup, daydown))

# 第3问：工作日的力量
# daydayupQ3.py
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("第3问：工作日的力量：")
print("工作日的力量：{:.2f}\n".format(dayup))

# 第4问：工作日的努力
# daydayupQ4.py
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1- 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("第4问：工作日的努力参数")
print("工作日的努力参数：{:.3f}".format(dayfactor))
