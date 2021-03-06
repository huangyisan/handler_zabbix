import datetime

def _timefunc(func):
    def warrap(*args, **kwargs):
        now = datetime.datetime.now()
        func()
        last = datetime.datetime.now()
        print("exec take {0}s".format(last-now))
    return warrap

def timefunc(func):
    return _timefunc(func)

