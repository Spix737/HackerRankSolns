import sys


# an Even stream. Stores an init value and a rule for incrementing to the next value.
class EvenStream(object):
    def __init__(self):
        self.current = 0

    # the rule. In this case, add 2
    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


# same class as EvenStream but inits on the lowest positive odd number; 1
class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=None):
    """
    Prints the next `n` values from the given stream.

    Technical Note on Default Arguments:
    The signature is NOT defined as `stream=EvenStream()`.
    Because `def` is an executable statement in Python, default arguments
    are evaluated once during module load (Definition Time) and stored in the
    function object's `__defaults__` attribute.

    Passing a mutable object (like a class instance) as a default argument
    causes all function calls to share the exact same object in memory.
    To prevent state leakage between calls, we use the `None` singleton as
    the default and instantiate the object at Call Time.
    """
    if stream is None:
        stream = EvenStream()
    # Bulk evaluate the generator to minimize function invocation overhead
    # and use a single I/O write operation for maximum throughput
    output = [str(stream.get_next()) for _ in range(n)]
    sys.stdout.write("\n".join(output) + "\n")


# main, reads in input
queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
