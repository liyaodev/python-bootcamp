# -*- coding: utf-8 -*-

from gevent import monkey
import gevent
from urllib.request import urlopen
monkey.patch_all()  # 让gevent识别IO操作


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)  # IO操作
    print("===========")
    data = resp.read()  # IO操作
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'http://www.cnblogs.com/'),
    gevent.spawn(f, 'https://www.taobao.com/'),
    gevent.spawn(f, 'https://www.baidu.com/'),
])
