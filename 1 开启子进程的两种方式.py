from multiprocessing import Process
import time
#方式一
# def text(name):
#     print('%s is run' %name)
#     time.sleep(5)
#     print('%s is done' %name)
#
# if __name__ == '__main__':
#     # Process(target = text, kwargs={name:'子进程1'})
#     p=Process(target=text,args=('子进程1',))
#     p.start() #只是给操作系统发送一个信号
#     # （然后操作系统申请内存空间，
#     # 把父进程的内存空间的地址拷贝给子进程，
#     # 作为子进程运行的初始状态）
#     print('主进程')


#方式二
class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s is run' %self.name)
        time.sleep(5)
        print('%s is done' %self.name)

if __name__ == '__main__':
    p=MyProcess('子进程1')
    p.start()
    print('主')