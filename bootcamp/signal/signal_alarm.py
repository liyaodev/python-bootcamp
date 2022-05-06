# -*- coding: utf-8 -
import signal

def alert_handler(signum, frame):
    print('Signal handler called with signal', signum)

# 1.设置定时信号
signal.signal(signal.SIGALRM, alert_handler)
print(signal.getsignal(s))
signal.alarm(3)

# 2.进程暂定，等待时钟信号
import time
time.sleep(10)

# 3.禁用定时信号
signal.alarm(0)
