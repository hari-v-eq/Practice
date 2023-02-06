import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(6)
    logging.info("Thread %s : stopped", name)

if __name__=="__main__":
    format= "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt= "%H:%M:%S")

    threads=[]
    for i in range(3):
        logging.info ("Main: creating and starting thread %d", i)
        x=threading.Thread(target=thread_function, args=(1,))
        threads.append(x)
        x.start()

    for i, thread in enumerate(threads):
        logging.info(" before joining thread %d ", i)
        thread.join()
        logging.info("Main : thread %d done ",i)

    # logging.info("main : before creating Thread")

    # x=threading.Thread(target=thread_function, args=(1,))
    # logging.info("main: running Thread")
    # x.start()
    # logging.info("main : wait for  thread to finish")
    # # x.join()
    # logging.info("Main : all Done")


