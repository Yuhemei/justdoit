# 对象属性管理
class ok:
    __slots__ = ('name','sex','age')
    def __init__(self):
        print('ok')
    # 把一个实例变成一个函数
    def __call__(self, *args, **kwargs):
        pass

print(abs(-1))
a=ok()
print(ok.__mro__)
# 可以被调用 callable
# 不可被调用对象

# 闭包，定义一个函数，将函数作为返回值
# 函数会开辟新的作用域
def range_it(a,b):

    for i in range(a,b,):
        return lambda :i*i
range_it(1,2)

# decorator
# 装饰器函数内部参数应该声明为不定长
print(14595+2279)
