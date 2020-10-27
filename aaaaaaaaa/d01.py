"""
父进程结束 进程池销毁
"""

from multiprocessing import Pool
from time import sleep,ctime
import random
#进程池时间函数
def worker(msg,sec):
    print(ctime(),"----",msg)
    sleep(sec)
#创建进程池
pool=Pool()
#向进程池队列中添加事件
for i in range(10):
    msg="tedu_%d"%i
    pool.apply_async(func=worker,
                     args=(msg,random.randint(1,4)))
#关闭进程池 不能添加新事件
pool.close()
#回收进程池
pool.join()