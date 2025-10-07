class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


StrongMan = Person("Ying")
StrongMan.add_friend("Lin")

# 创建两个 Person 实例
Ying = Person("Ying")
peter = Person("Peter")
huang = Person("huang")
huang2 = Person("huangzhen")
# Mary 添加 Peter 为朋友
Ying.add_friend(peter)
Ying.add_friend(huang)
Ying.add_friend(huang2)
# Peter 添加 Mary 为朋友
peter.add_friend(Ying)

# 打印 Mary 和 Peter 的朋友列表
print(f"{Ying.name}'s friends: {[friend.name for friend in Ying.friends]}")
print(f"{peter.name}'s friends: {[friend.name for friend in peter.friends]}")

# 在 for 循环中，friend.name 被解释为一个变量名，而不是一个属性访问表达式。
# Python 会尝试将 Ying.friends 中的每个元素赋值给 friend.name，这显然不是你想要的效果。
# 如果写成for friend.name in Ying.friends，有错误，解释为上两行

for friend in Ying.friends:
    print(friend.name)

# 在 Python 中，f-string（格式化字符串）中的表达式可以包含任何有效的 Python 代码，包括列表推导式。
# 列表推导式的语法是 [expression for variable in iterable]。
# expression 是要生成的值。
# for variable in iterable 是循环部分，用于遍历可迭代对象。