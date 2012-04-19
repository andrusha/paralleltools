"""
     +----------------+
     | AbstractWorker |
     +----------------+
        ^         ^
        |         |
+-------+---+ +---+----------+
| MapWorker | | FilterWorker |
+-----------+ +--------------+

http://www.asciiflow.com/#8469284594412873285/1889361939
"""

import threading

class AbstractWorker(threading.Thread):
    def __init__(self, function, work_queue, result_queue, result_callback):
        super(AbstractWorker, self).__init__()
        self.function = function
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.result_callback = result_callback
        self.stopped = False

    def run(self):
        while True:
            if self.stopped:
                break

            try:
                item = self.work_queue.get()
                self.process(item)
            finally:
                self.work_queue.task_done()

    def stop(self):
        self.stopped = True

    def process(self, item):
        raise NotImplementedError('You should implement processing function first')

class FilterWorker(AbstractWorker):
    def process(self, item):
        if self.function(item):
            self.result_queue.append(item)
            if self.result_callback is not None:
                self.result_callback(item)

class MapWorker(AbstractWorker):
    def process(self, item):
        result = self.function(item)
        self.result_queue.append(result)
        if self.result_callback is not None:
            self.result_callback(result)
