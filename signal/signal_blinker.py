# -*- coding: utf-8 -

from blinker import Namespace

# 1.定义信号
namespace = Namespace()
fire = namespace.signal("fire")

# 2.定义一个回调函数，里面至少要接收一个参数
def open_fire(sender, a, b, c):
    print(sender, a, b, c)
    print("open fire")

fire.connect(open_fire)

# 如果有多个参数，参数需要通过关键字参数指定传递
fire.send("xxx", a=1, b=2, c=3)
# 第一个参数不指定，则默认传了一个None进去
fire.send(a=1, b=2, c=3)
