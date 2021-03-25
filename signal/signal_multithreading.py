# -*- coding: utf-8 -
import signal
import threading
import os
import time

def usr1_handler(num, frame):
    print("received signal %s %s" % (num, threading.currentThread()))

signal.signal(signal.SIGUSR1, usr1_handler)

def thread_get_signal():
    # 如果在子线程中设置signal的handler 会报错
    # ValueError: signal only works in main thread
    # signal.signal(signal.SIGUSR2, usr1_handler)

    print("waiting signal", threading.currentThread())
    # sleep 进程直到接收到信号
    signal.pause()
    print("waiting done")

receiver = threading.Thread(target=thread_get_signal, name="receiver")
receiver.start()
# 为了保证线程开启顺利，加0.1s延迟
time.sleep(0.1)

pid = os.getpid()
print('pid', pid)

def send_signal():
    print("sending signal", threading.currentThread())
    os.kill(pid, signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name="sender")
sender.start()
sender.join()

# 为了让程序结束，唤醒 pause
signal.alarm(1)
receiver.join()
