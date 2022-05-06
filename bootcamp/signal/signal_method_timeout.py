# -*- coding: utf-8 -

# From https://github.com/breenmachine/httpscreenshot/blob/master/httpscreenshot.py#L41
def timeoutFn(func, args=(), kwargs={}, timeout_duration=1, default=None):
    import signal

    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError()

    # set the timeout handler
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_duration)
    try:
        result = func(*args, **kwargs)
    except TimeoutError as exc:
        result = default
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

    return result

def test_demo():
    import time
    time.sleep(10)

print(timeoutFn(test_demo, timeout_duration=3, default=9999))