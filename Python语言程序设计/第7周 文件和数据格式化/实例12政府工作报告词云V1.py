# 基本思路
# 步骤1：读取文件，分词整理
# 步骤2：设置并输出词云
# 步骤3：观察结果，优化迭代

# GovRptWordCloudV1.py
import jieba
import wordcloud

f = open("关于实施乡村振兴的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc",
                        width=1000, height=700,
                        background_color="white",
                        max_words=15)#设定15个词
w.generate(txt)
w.to_file("xcwordcloud15.png")
