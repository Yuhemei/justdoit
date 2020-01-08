# 导入正则表达式
import re

# 匹配方法
# 在第二个变量里找有没有第一个
m_init=re.match('My', 'My name is Ok')
m_init.group()
print(m_init)
print(m_init.group())

# 定义一个规则(定义正则）
# a-z里一个或多个小写字母
p_init=re.compile('[a-z]+')
r_init=p_init.match('hello999')
print(r_init.group())
r2_init=p_init.match('My')
print(r2_init)
if r2_init:
    print('ok')
else:
    print('none')

# search()只查第一个，从左往右第一个，首字母找不到还继续找
# findall()或finditer()找所有的
p2_init=re.compile('\d+/\d+/\d+')
s_init='Today is 11/27/2012. PyCon starts 3/13/2013'
r3_init=p2_init.findall(s_init)
print(r3_init)
# 可被调用的迭代器
r4_init=p2_init.finditer(s_init)
print(r4_init)
for i in r4_init:
    print(i.group())
# split（）进行切分 split('字符'，int)
line='dsafcdsfdas  ,dsfsdds ,,, wtrsedtrfds ;;;fdhfddfhfd '
# 正则切分文档
line=line.strip()
l_init=re.split(r'[;,\s]+\s*',line)
print(l_init)
# re.sub（）进行替换

print(i)
