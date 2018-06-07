from threading import Thread, Lock
import random
import time
class Generator(Thread):
    def __init__(self):
        self.num = None
        super(Generator, self).__init__()
    def run(self):
        global queue
        while(True):
            self.num = random.randint(1, 10)
            lock.acquire()
            qsq.append(self.num)
            qcu.append(self.num)
            print("Random number:", self.num)
            lock.release()
            time.sleep(1)

class Square(Thread):
    def __init__(self):
        super(Square, self).__init__()
    def run(self):
        global queue
        while(True):
            lock.acquire()
            try:
                num = qsq.pop(0)
                print("Square:", num ** 2)
            except:
                continue
            finally:
                lock.release()
class Cube(Thread):
    def __init__(self):
        super(Cube, self).__init__()
    def run(self):
        global queue
        while(True):
            lock.acquire()
            try:
                num = qcu.pop(0)
                print("Cube:", num ** 3)
            except:
                continue
            finally:
                lock.release()


if __name__ == '__main__':
    qsq = []
    qcu = []
    lock = Lock()
    g = Generator()
    s = Square()
    c = Cube()
    g.start()
    s.start()
    c.start()
