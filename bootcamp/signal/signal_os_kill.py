# -*- coding: utf-8 -
import signal
import os
import time

# 执行打印
def receive_signal(signum, stack):
    print('Received:', signum)

def do_exit(signum, stack):
    print('Received:', signum)
    raise SystemExit('Exiting')

# 设置用户自定义信号 1
signal.signal(signal.SIGUSR1, receive_signal)
# 设置用户自定义信号 2
signal.signal(signal.SIGUSR2, do_exit)

print('My PID is:', os.getpid())
while True:
    print('Waiting...')
    time.sleep(3)