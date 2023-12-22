
class Broker(object):
    # 任务队列
    broker_list = []

class Worker(object):
    # 任务执行者
    def run(self,broker,func):
        if func in broker.broker_list:
            func()
        else:
            return 'error'

class Celery(object):
    def __init__(self):
        self.broker = Broker()
        self.worker = Worker()
    def add(self,func):
        self.broker.broker_list.append(func)
    def work(self,func):
        self.worker.run(self.broker,func)

def send_sms_code():
    print('send_sms_code')

app = Celery()#创建celery实例
app.add(send_sms_code)#添加任务
app.work(send_sms_code)#worker执行任务