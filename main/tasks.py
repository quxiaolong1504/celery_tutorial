# encoding:utf-8
import time
from celery.task import task

@task
def _do_kground_work(name):
    """
    这里用time 模拟耗时操作
    """
    for i in range(1,10):
        print 'hello:%s  %s'%(name,i)
        time.sleep(1)