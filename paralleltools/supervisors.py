"""
    Supervisor is inspired by Erlang, it's a process
    which runs in background and if one thread is died
    it will restart it.
    Or propagate "stop" signal if necessary
"""

import sys
import time
import threading

if sys.version_info >= (3, 0):
    import queue as Queue
    xrange = range
else:
    import Queue


class Supervisor(threading.Thread):
    def __init__(self, klass, params, work_queue, threads):
        super(Supervisor, self).__init__()
        self.work_queue = work_queue
        self.threads = Queue.Queue()
        self.klass = klass
        self.params = params
        self.stopped = False

        if threads < 1:
            raise ValueError("You must run at least one thread")

        for _ in xrange(threads):
            self.spawn_thread()

    def spawn_thread(self):
        thread = self.klass(*self.params)
        thread.daemon = True
        thread.start()
        self.threads.put(thread)

    def run(self):
        while True:
            if self.stopped:
                break

            #respawn dead threads every second
            time.sleep(1)
            if not self.work_queue.empty():
                try:
                    thread = self.threads.get()
                    if not thread.is_alive():
                        self.spawn_thread()
                    else:
                        self.threads.put(thread)
                finally:
                    self.threads.task_done()

    def stop(self):
        self.stopped = True
        while not self.threads.empty():
            thread = self.threads.get()
            thread.stop()
