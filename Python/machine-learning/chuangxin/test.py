import re
import jieba.analyse
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#这个文件是统计频率时，把需要过滤的词放到这个文件里面
# invalid_words_file = "invalidwords.txt"


def get_Words():
    #读取TXT文件获取文本里的内容
    with open("threekingdom.txt", encoding='utf-8') as f:
        qzgs_text = f.read()
    #制定正则规则，把各种符号去掉，最后生成没有各种符号的字符串
    pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
    new_qzgs_text = pattern.sub("", qzgs_text)

    #获取分词
    qzgs_words = [word for word in jieba.cut(new_qzgs_text, cut_all=False) if len(word) > 2]

    # #设置停用词
    # jieba.analyse.set_stop_words(invalid_words_file)
    #
    # #获取关键词频率
    # tags = jieba.analyse.extract_tags(qzgs_text,topK=100,withWeight=True)
    # for tag in tags:
    #     print(tag)

    #制定需要过滤的词
    invalid_words_zh = ["所有人", "看起来", "小说网", "是不是", "为什么", "没什么", "其他人", "未完待续",
                        "事实上", "一时间", "是因为", "一瞬间", "只不过", "差不多", "不至于", "这时候", "越来越", "没想到", "可不是", "不得不", "接下来",
                        "魄之力", "俱乐部", "挑战赛", "全明星", "擂台赛", "季后赛","boss", "wwwmianhuatangla",]

    #进行过滤操作
    for word in qzgs_words:
        if word in invalid_words_zh:
            qzgs_words.remove(word)

    # 获取分词频数
    c = Counter(qzgs_words)
    for word in c.most_common(5):
        word,freq = word
        print(word,freq)
    print(qzgs_words)
    print(c.most_common(5))
get_Words()