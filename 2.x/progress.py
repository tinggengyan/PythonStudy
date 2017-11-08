# -*- coding: utf-8 -*-
import os
from multiprocessing import Process


# 子进程执行的代码
def run_progress(name):
    print 'Run child progress %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
    print 'Parent progress %s.' % os.getpid()
    p = Process(target=run_progress, args=('test',))
    print 'progress will start'
    p.start()
    p.join()
    print 'Progress end'
