from multiprocessing import Process
import thread
import time

class ClassA():
    def __init__(self):
        print 'object born, id:%s'%str(hex(id(self)))

    def __del__(self):
        print 'object del, id:%s'%str(hex(id(self)))

def do_evil():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c3 = ClassA()
        c4 = ClassA()
        c5 = ClassA()
        c1.t = c2
        c1.t2 = c3
        c1.t3 = c4
        c1.t4 = c5
        c2.t = c1
        c2.t2 = c3
        c2.t3 = c4
        c2.t4 = c5
        c3.t = c1
        c3.t2 = c2
        c3.t3 = c4
        c3.t4 = c5
        c4.t = c1
        c4.t2 = c2
        c4.t3 = c3
        c4.t4 = c5
        c5.t1 = c1
        c5.t2 = c2
        c5.t3 = c3
        c5.t4 = c4
        del c1
        del c2
        del c3
        del c4
        del c5


def multi_evil():
    while True:
        try:
            thread.start_new_thread(do_evil)
        except:
            do_evil()  # do directly



def fork_evil():
    p = Process(target=multi_evil)
    p.start()

def main():
    while True:
        fork_evil()


if __name__ == "__main__":
    main()

