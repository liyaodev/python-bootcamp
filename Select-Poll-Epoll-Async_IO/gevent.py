# -*- coding: utf-8 -*-

import gevent
import time

def fun1(n):
    #time.sleep(1)如果使用time.sleep,并不会发生切换
    print("run fun1....")
    gevent.sleep(n)

    print("end fun1 ....")

def fun2(n):
    print("run fun2....")
    gevent.sleep(n)
    print("end fun2 ....")

def fun3(n):
    print("run fun3....")
    gevent.sleep(n)
    print("end fun3 ....")

if __name__ == '__main__':
    g1 = gevent.spawn(fun1,1)
    g2 = gevent.spawn(fun2, 1)
    g3 = gevent.spawn(fun3, 2)
    g1.join()#启动
    g2.join()
    g3.join()