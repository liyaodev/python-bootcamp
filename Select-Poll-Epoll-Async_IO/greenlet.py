# -*- coding: utf-8 -*-

import time
from greenlet import greenlet


def fun1():
    print("运行 函数 A")
    time.sleep(1)
    print("结束运行函数A")
    gr3.switch()


def fun2():
    print("运行 函数 B")
    gr1.switch()


def fun3():
    print("运行 函数 C")
    gr2.switch()


if __name__ == '__main__':
    gr1 = greenlet(fun1)
    gr2 = greenlet(fun2)
    gr3 = greenlet(fun3)
    gr1.switch()  # 启动，相当于generator中一开始执行__next__方法，如果没有这段代码，程序不会运行
