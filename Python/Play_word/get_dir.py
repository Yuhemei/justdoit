#读取文件并操作文件对象
#将所有符号替换为空格
# 拆分源文中的单词
# 对单词进行计数
# 对单词以计数为基准进行排序
# 输出top100

# 导入的包
from collections import Counter
#载入需要的模块
import pandas as pd
import numpy as np
import os


#读取文件并操作文件对象

data_path=os.getcwd()  #获取当前工作路径，查看是否是自己的目标路径
# os.chdir('/Users/Heihei/Desktop/EX2data/data')  #如果不是，改到目标路径
# path = '/Users/Heihei/Desktop/EX2data/data'
os.chdir('word_object')
data_path=os.getcwd()  #获取当前工作路径
# data_path=os.listdir() #查看目标路径下有哪些数据
# print(data_path)

# 将所有文件的文件内容放到一个文件内
# 列表可视化当前文件名
datalist = []
for i in os.listdir(data_path):
    if os.path.splitext(i)[1] == '.txt':     #选取后缀为txt的文件加入datalist
        datalist.append(i)
print(datalist)  #查看datalist

#将数据整合到一个文件中
path=os.getcwd()
df = pd.DataFrame()
for txt in datalist:
    data_path_init = os.path.join(path,txt)    #列出path路径下目标文件的绝对路径，将其赋值给data_path_init
    df_txt = pd.read_table(data_path_init,index_col = False,error_bad_lines=False,encoding='gbk') #读取目标txt文件，不把原Data第一列作为索引
    df_txt['sub_n'] = txt[:2]    #取出前面的数值，并赋值给sub_n这一列（合并后我需要知道哪些数据来自哪个文件）
    # df_txt_sx = df_txt[df_txt['split'].isin([1,2])]  #用isin方法进行数据筛选（我的数据中split一列有3个值，我只需要改列值为1，2的行，其他行不需要）
    df = pd.concat([df,df_txt],axis=0, ignore_index=True,sort=False)     #（将筛选后的数据加到df框中。axis=0表示上下合并，axis=1表示左右合并，ignore_index=True表示忽略原来索引。除了concat函数外，也可以用df.append实现，但是还要改索引，比concat方法会麻烦点）

print(df)
# 保存文件
df.to_csv(r'word_init\word_init.data',index=False)
# index=False 表示不保存索引数据
#之后如果要读取的话，直接df.read_csv('word_init', index_col=False)就能得到 df框。
pd.read_csv('word_init.data', index_col=False)
#将所有符号替换为空格

# 拆分源文中的单词
# 对单词进行计数
# 对单词以计数为基准进行排序
# 输出top100
