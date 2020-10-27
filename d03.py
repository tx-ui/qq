from  multiprocessing import Process,Queue

q=Queue(2)

def put():
    user="lily"
    password="123456"
    q.put(user)
    q.put(password)
def get():
    name=q.get()
    password=q.get()
    print("姓名：",name)
    print("密码：",password)
p01=Process(target=put)
p02=Process(target=get)
p01.start()
p02.start()
p01.join()
p02.join()