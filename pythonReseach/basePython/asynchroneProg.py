
#coding:utf-8
import time
import threading

#programmation parallelle
my_lock = threading.RLock()

class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def cisco(self):
        i=0
        while (i < 3):
            with my_lock:
                letters="ABC"
                for lt in letters:
                    print(lt)
                    time.sleep(0.3)
            i+=1


th1=MyProcess()
th1.cisco()
th2=MyProcess()
th2.cisco()
th1.start()
th2.start()

th1.join()
th2.join()




"""
def processOne():
    i= 0
    while i < 3:
        print("000000")
        time.sleep(0.3)
        i += 1

def processTwo():
    i= 0
    while i < 3:
        print("XXXXXXXXXX")
        time.sleep(0.3)
        i += 1


th1 = threading.Thread(target=processOne)
th2 = threading.Thread(target=processTwo)

th1.start()
th2.start()

th1.join()
th2.join()

"""

print("fin du programme")









