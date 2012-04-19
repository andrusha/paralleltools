import sys
if sys.version_info >= (3, 0):
    import queue as Queue
else:
    import Queue

from paralleltools.workers import FilterWorker, MapWorker
from paralleltools.supervisors import Supervisor

all = ['filter', 'map', 'aync_filter', 'async_map']

def filter(function, iterable, threads=5, result_callback=None):
    return _start_worker(FilterWorker,
                         function,
                         iterable,
                         threads,
                         result_callback,
                         async=False)

def map(function, iterable, threads=5, result_callback=None):
    return _start_worker(MapWorker,
                         function,
                         iterable,
                         threads,
                         result_callback,
                         async=False)

def async_filter(function, iterable, threads=5, callback=None):
    return _start_worker(FilterWorker,
                         function,
                         iterable,
                         threads,
                         callback,
                         async=True)

def async_map(function, iterable, threads=5, callback=None):
    return _start_worker(MapWorker,
                         function,
                         iterable,
                         threads,
                         callback,
                         async=True)

def _start_worker(worker_cls, function, iterable, threads=5, result_callback=None, async=False):
    work_queue = Queue.Queue()
    result_queue = []

    supervisor = Supervisor(worker_cls, [function, work_queue, result_queue, result_callback], work_queue, threads)
    supervisor.daemon = True
    supervisor.start()

    for item in iterable:
        work_queue.put(item)

    if not async:
        work_queue.join()
        del supervisor

        return result_queue
    else:
        return supervisor
