import time


def ensure_execution(func):
    def inner(*args, **kwargs):
        while 1:
            try:
                func(*args, **kwargs)
                break
            except:
                time.sleep(0.01)
    return inner