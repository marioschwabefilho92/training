import trace


def calculate():
    c = 10+20
    return c


# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(trace=False)


# run the new command using the given tracer
# tracer.runfunc(calculate)


# count number of executions
a = 10
while a > 0:
    tracer.runfunc(calculate)
    nmb_exec = (list(tracer.counts.values())[0])
    print(nmb_exec)
    a -= 1 