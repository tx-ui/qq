"""
练习1 ：  使用进程池完成
拷贝一个指定的目录 （文件夹中全是普通文件没有子文件夹）

思路 ： 1. 什么事情作为进程池事件  （拷贝文件）
       2. 拷贝文件函数  找共性封装  特性传参

       os.listdir()
       os.mkdir("xxx")
"""

from multiprocessing import Pool,Queue
import os
q=Queue()


def getsize(old_folder):
    totalsize=0
    for item in old_folder:
        totalsize+= os.path.getsize(item)
    return totalsize


# 拷贝每一个文件 --》 进程池要做的事情
def copy(filename,old_folder,new_folder):
    fr = open(old_folder+"/"+filename,'rb')
    fw = open(new_folder+"/"+filename,'wb')

    # c=0
    while True:
        data = fr.read(1024)

        if not data:
            break
        n=fw.write(data)
        q.put(n)
    fr.close()
    fw.close()



# 创建进程池 参数为要拷贝的目录
def main(old_folder):
    # 创建新文件夹
    new_folder = old_folder + "-备份"
    os.mkdir(new_folder)

    pool = Pool(4)
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,
                         args=(file,old_folder,new_folder))

    pool.close()
    copysize=0
    while copysize<totalsize:
        copysize+=q.get()
        print("已拷贝：%f.2%%"%(copysize/totalsize*100))

    pool.join()


if __name__ == '__main__':
    main("/home/tarena/FTP")






