import sys
import trace


def calculate():
    c = 10+20
    return c


# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)


# run the new command using the given tracer
tracer.run('calculate()')
tracer.runfunc(calculate)


# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")

