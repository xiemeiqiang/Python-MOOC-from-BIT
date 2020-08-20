# 基本思路
# 步骤1：读取文件，分词整理
# 步骤2：设置并输出词云
# 步骤3：观察结果，优化迭代

# GovRptWordCloudV2.py
# 设置形状
import jieba
import wordcloud
from scipy.misc import imread  # scipy.misc.imread()被弃用,程序报错
mask = imread("fivestars.png")

f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc",
                        width=1000, height=700,
                        background_color="white",
                        mask=mask)#指定形状
w.generate(txt)
w.to_file("grwordcloudV2.png")
