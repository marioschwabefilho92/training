import sys

try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except:
    err = sys.exc_info()
    for e in err:
        print(e)
