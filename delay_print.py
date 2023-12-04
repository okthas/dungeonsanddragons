import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        if s == "Saving...":
            time.sleep(0.1)
        else:
            time.sleep(0.02)
