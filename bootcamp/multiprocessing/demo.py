# -*- coding: utf-8 -*-

from multiprocessing import Pipe, Process

def do_process(x, pipe):
    _out_pipe, _in_pipe = pipe
    # 关闭fork过来的输入端
    _in_pipe.close()
    while True:
        try:
            msg = _out_pipe.recv()
            print(msg)
        except EOFError:
            # 当out_pipe接受不到输出的时候且输入被关闭的时候，会抛出EORFError，可以捕获并且退出子进程
            break


if __name__ == '__main__':
    out_pipe, in_pipe = Pipe(True)
    do_p = Process(target=do_process, args=(100, (out_pipe, in_pipe)))
    do_p.start()

    # 等pipe被fork后，关闭主进程输出端
    # 这样创建端Pipe一端连着主进程输入，一端连着子进程输出
    out_pipe.close()
    for x in range(10):
        in_pipe.send(x)
    in_pipe.close()
    do_p.join()
    print("主进程结束")
