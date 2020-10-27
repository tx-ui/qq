#使用进程池完成 拷贝一个指定的目录（文件夹中全是普通文件没有子文件夹）


from multiprocessing import Pool
from time import sleep
import os
#获取文件名字
list_file=os.listdir("/home/tarena/桌面month02/i/day04")#../../day04

#创建一个新文件夹
os.mkdir("/home/tarena/桌面month02/i/day13/copydir")

#进程池事件,复制文件函数
def copy(old_mulu,sec):
    #打开文件路径
    for item in os.listdir(old_mulu):
        file_obj=open("%s"%item,"r")
    #在新文件夹中创建一个同名文件
    print(ctime(),"----",msg)
    sleep(sec)


def main():
    #创建进程池
    pool=Pool()
    #向进程池队列中添加事件
    for item in os.listdir(old_mulu):
        pool.apply_async(func=copy,args=(filename))
    #关闭进程池 不能添加新事件
    pool.close()
    #回收进程池
    pool.join()

if __name__ == '__main__':
    main()










