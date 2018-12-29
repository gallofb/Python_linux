import os
import time

def child():
    print('son :',os.getpid())
    print('parents id is',os.getppid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        print(newpid)
        if newpid ==0:
            child()
        else:
            pids = (os.getpid(),newpid)
            print("parent:%d,child:%d"%pids)
            print("parent parent:",os.getppid())

        if input() == 'q':
            break
        else:
            continue

parent()


