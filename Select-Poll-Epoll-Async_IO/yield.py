# -*- coding: utf-8 -*-

import time


def consumer(name):
    print("%s消费者启动。。。" % name)
    r = " "
    while True:
        new_food = yield r      # 通过 yeild 向生产者发送消息
        print("[%s]消费者获取到[%s]" % (name, new_food))
        r = name


def product():
    con.__next__()              # 先执行 __next__ 方法启动生成器
    con1.__next__()
    n = 0
    while n < 5:
        print("生产者启动。。。")
        r1 = con.send(n)        # 向生成器 consumer 发送消息并激活生成器
        r2 = con1.send(n)
        print("生产者推送 %s 完成" % r1)
        print("生产者推送 %s 完成" % r2)
        n += 1
        time.sleep(1)
    con.close()
    con1.close()


if __name__ == '__main__':
    con = consumer("A")
    con1 = consumer("B")
    p = product()
