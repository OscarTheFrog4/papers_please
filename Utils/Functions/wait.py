import time

def wait(secs=0, lines=0):
    time.sleep(secs)
    for i in range(lines):
        print()