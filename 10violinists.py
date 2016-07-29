import threading
import queue
import time


class Violinist(threading.Thread):
    def __init__(self, queue_violin, queue_bow, mutex_violin, mutex_bow, name):
        threading.Thread.__init__(self)
        self.queue_violin = queue_violin
        self.queue_bow = queue_bow
        self.mutex_violin = mutex_violin
        self.mutex_bow = mutex_bow
        self.name = name

        if self.queue_violin.full():
            pass
        else:
            self.queue_violin.put('violin')

        if self.queue_bow.full():
            pass
        else:
            self.queue_bow.put('bow')

    def run(self):
        while True:
            self.mutex_violin.acquire()
            while self.queue_violin.qsize() == 0:
                self.mutex_violin.wait()
            print('The violinist ' + self.name + ' take a violin.')
            self.queue_violin.get()
            self.mutex_violin.notifyAll()
            self.mutex_violin.release()

            self.mutex_bow.acquire()
            while self.queue_bow.qsize() == 0:
                self.mutex_bow.wait()
            print('The violinist ' + self.name + ' take a bow.')
            self.queue_bow.get()
            self.mutex_bow.notifyAll()
            self.mutex_bow.release()

            print('The violinist ' + self.name + ' playing...')
            time.sleep(2)

            self.mutex_violin.acquire()
            while self.queue_violin.qsize() >= 5:
                self.mutex_violin.wait()
            print('The violinist ' + self.name + ' put a violin')
            self.queue_violin.put('violin')
            self.mutex_violin.notifyAll()
            self.mutex_violin.release()

            self.mutex_bow.acquire()
            while self.queue_bow.qsize() >= 5:
                self.mutex_bow.wait()
            print('The violinist ' + self.name + ' put a bow')
            self.queue_bow.put('bow')
            self.mutex_bow.notifyAll()
            self.mutex_bow.release()


def main():
    que_violin = queue.Queue(maxsize=5)
    que_bow = queue.Queue()
    mutex_violin = threading.Condition()
    mutex_bow = threading.Condition()
    v1 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v1')
    v2 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v2')
    v3 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v3')
    v4 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v4')
    v5 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v5')
    v6 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v6')
    v7 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v7')
    v8 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v8')
    v9 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v9')
    v10 = Violinist(que_violin, que_bow, mutex_violin, mutex_bow, 'v10')
    v1.start()
    v2.start()
    v3.start()
    v4.start()
    v5.start()
    v6.start()
    v7.start()
    v8.start()
    v9.start()
    v10.start()

main()
