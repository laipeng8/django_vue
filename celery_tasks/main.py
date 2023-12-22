"""
生产者
# 生产者---任务
# 1这个函数 必须要让celery的实例的task装饰器装饰
# 2 需要celery 自动吉娜
册指定包的任务

from libs.yuntongxun.sms import CCP
from celery_tasks.main import app

@app.task
def celery_send_sms_code(mobil,code):
    # CCP().send_template_sms(mobil,[code,5],1)
    CCP().send_template_sms(mobil, [code, 5], 1)

# 3需要celery 自动检测指定包的任务
# autodiscover_tasks里的参数是列表
# 列表中的元素是tasks的路进
app.autodiscover_tasks(['celery_tasks.sms'])


消费者：
celery -A proj worker -l INFO
在虚拟环境中执行
celery -A celery实例的脚本路径 worker -l INFO


队列
# 2设置broker
# 通过加载配置文件设在broker
app.config_from_object('celery_tasks.config')
# 配置信息，key  = value
# 我们指定redis为我们的中间人（队列）
broker_url = "redis://127.0.0.1:6379/15"

celery -将这三者实现


"""
import os

# 为django的celery设置环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_vue.settings')

# 1创建celery的实例
from celery import Celery
#参数1  main 设置脚本路径就可以了   脚本路径是唯一的
app = Celery('celery_tasks')

# 2设置broker
# 通过加载配置文件设在broker
app.config_from_object('celery_tasks.config')

# 3需要celery 自动检测指定包的任务
# autodiscover_tasks里的参数是列表
# 列表中的元素是tasks的路进
app.autodiscover_tasks(['celery_tasks.sms'])









