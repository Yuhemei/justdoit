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
    with open("all.txt", encoding='utf-8') as f:
        qzgs_text = f.read()
    #制定正则规则，把各种符号去掉，最后生成没有各种符号的字符串
    pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
    new_qzgs_text = pattern.sub("", qzgs_text)

    #获取分词
    qzgs_words = jieba.lcut(new_qzgs_text,cut_all=False)
    count = {}
    for word in qzgs_words:
        if len(word) <= 1:
            continue
        else:
            # 将词存入count  字典  K-V
            # {曹操 ：888，'将军':777}
            # count[word] = '取字典里面的这个键对应的值'+1
            # count[word] = count[word] + 1
            count[word] = count.get(word, 0) + 1
    print(len(count))
    # 将指代相同的词进行合并
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
    # 输出前几
    c = Counter(qzgs_words)
    for word in c.most_common(5):
        word,freq = word
        print(word,freq)
    print()

    w_l = list(count.items())
    # 排序字典中的value
    w_l.sort(key=lambda x: x[1], reverse=True)
    print(w_l)
    # 展示前20的词汇
    role_list = []
    for i in range(30):
        role, counts = w_l[i]
        role_list.append(role)
    role_txt = ' '.join(role_list)
    print(role_list)
    print(role_txt)
    return role_txt

def generate_wc(data):
    # 字体路径
    path = "C:/Windows/Fonts/STFANGSO.ttf"
    # 读入背景图片
    bg_pic = np.array(Image.open('twice.png'))
    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(bg_pic)
    # 生成词云,后面的generate是根据文本生成词云
    wc = WordCloud(background_color="black", font_path=path, mask=bg_pic, color_func=image_colors)
    wc = wc.generate(data)
    # 显示词云图片
    plt.imshow(wc)
    plt.axis("off")
    # axis函数接收一个list，设定横纵坐标尺度，list各个参数分别代表[X初始刻度，X终止刻度，Y起始刻度，Y终止,off就是不显示坐标尺寸
    plt.show()
    # 保存图片
    wc.to_file("result-all.jpg")


if __name__ =="__main__":
    data=get_Words()
    generate_wc(data)

