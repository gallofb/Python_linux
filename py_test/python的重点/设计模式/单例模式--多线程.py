import threading
class Singleton:
    _instance_lock = threading.Lock()
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            with cls._instance_lock:
                if cls._instance == None:
                    cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self,name):
        self.name = name



def run():
    sig = Singleton("zhu")
    print(sig,sig.name)
# sig1 = Singleton("zhu")
# sig2 = Singleton("hu")
for i in range(10):
    t = threading.Thread(target=run,)
    t.start()
