# 私有变量可以修改
class Cat:
    '''一个猫类'''

    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def __str__(self):
        print("干的漂亮！")
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    # p = property(getAge, setAge)

    def eat(self):
        print(f"小猫爱吃鱼，我是{self.name},self的地址是{id(self)}")

    def drink(self):
        print("它在喝水")

try:
    cat = Cat('小猫',19)
    cat.eat()
    cat.p=18
    cat.p
    print(cat.p)
except:
    print("请输入正确的信息：")
