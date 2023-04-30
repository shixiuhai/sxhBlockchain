# https://juejin.cn/post/6844903568823025678
# https://github.com/xilibi2003/blockchain
import requests
import time
import queue
from concurrent.futures import ThreadPoolExecutor
# 重新封装线程池类
class ThreadPoolExecutor(ThreadPoolExecutor):
    """
    重写线程池修改队列数
    """
    def __init__(self, max_workers=None, thread_name_prefix=''):
        super().__init__(max_workers, thread_name_prefix)
        # 队列大小为最大线程数的两倍
        self._work_queue = queue.Queue(self._max_workers * 2)

pool = ThreadPoolExecutor(max_workers=1)
start_time=time.time()

def get_retquest():
    print(requests.get("http://104.225.236.140:5000/mine").text)
 
while True:
    pool.submit(get_retquest)
    end_time=time.time()
    if end_time-start_time>1800:
        start_time=end_time
        print("--------------------开始同步--------------------")
        requests.get("http://104.225.236.140:5001/nodes/resolve")
        print("--------------------同步成功--------------------")