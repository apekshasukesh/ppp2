from ruffus import *
import sys
import time
class time_job(object):
    """The time_job decorator wraps a function and prints elapsed time to standard
    out, or any other file-like object with a .write() method.
    """
    def __init__(self, stream=sys.stdout):
        self.stream = stream
    def __call__(self, func):
        def inner(*args, **kwargs):
            # Start the timer.
            start = time.time()
            # Run the decorated function.
            ret = func(*args, **kwargs)
            # Stop the timer.
            end = time.time()
            elapsed = end - start
            name = func.__name__
            self.stream.write("{} took {} seconds\n".format(name, elapsed))
            # Return the decorated function's return value.
            return ret
        inner.__name__ = func.__name__
        if hasattr(func, "pipeline_task"):
            inner.pipeline_task = func.pipeline_task
        return inner



@time_job(sys.stderr)
def first_task():
    print "First task"


@time_job(sys.stderr)
@follows(first_task)
def second_task():
    print "Second task"


@time_job(sys.stderr)
@follows(second_task)
def final_task():
    print "Final task"

pipeline_run()
