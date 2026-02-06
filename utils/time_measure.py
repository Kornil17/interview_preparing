from time import perf_counter


def timer(f):
    def _timer(*args, **kwargs):
        start = perf_counter()
        res = f(*args, **kwargs)
        print("Time result: ", perf_counter() - start)
        return res

    return _timer