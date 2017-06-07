import sys
import time

f=None
try:
    f=open("peom.txt")
    # Our usual file-reading idiom
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line,end="")
        sys.stdout.flush()
        print("Press ctrl+c now")
        # To make sure it runs for a while
        time.sleep(2)
except FileNotFoundError:
    print("Could not find file peom.txt")
except EOFError:
    print("Could not find file peom.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
