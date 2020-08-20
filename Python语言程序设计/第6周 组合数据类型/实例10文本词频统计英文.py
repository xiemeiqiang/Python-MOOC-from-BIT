# CalHamletV1.py

def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '|"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getText()
words = hamletTxt.split() #split方法用空格分隔hamletTxt文本，words 是一个列表
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
    # d.get(k, <default>) 键k存在，则返回相应值，不在则返回<default>值
    # 英文单词为键，出现次数为对应的值
    # counts.get(word, 0)用当前的某一个英文单词作为键，索引字典，如果在，返回次数+1，
    # 如果单词不在字典中，那就加到字典中，并赋默认值0+1，表示在字典中出现了一次
items = list(counts.items())
# d.items() 返回字典中所有的键值对信息
items.sort(key=lambda x:x[1], reverse=True)
# 对一个列表，按照键值对的两个元素的第二个元素进行排序，排序的默认方式是由大到小的倒叙，reverse=True，修改为由大到小
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:<5}".format(word, count))
    # 冒号是引导符，后面跟的是格式控制方法。<表示左对齐，>表示右对齐，数字表示宽度。
