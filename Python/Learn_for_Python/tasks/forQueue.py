import threading
import  time
def a1():
    time.sleep(2)
    print('线程1')
def a2():
    time.sleep(15)
    print('线程2')
if __name__=='__main__':
    t1=threading.Thread(target=a1)
    t2=threading.Thread(target=a2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(4)
