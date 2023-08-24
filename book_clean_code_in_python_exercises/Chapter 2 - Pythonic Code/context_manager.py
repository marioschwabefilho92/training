fd = open(filename)
try:
    process_file(fd)
finally:
    fd.close()


with open(filename) as fd:
    process_file(fd)