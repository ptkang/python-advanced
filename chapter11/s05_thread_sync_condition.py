# 线程同步-条件变量：Condition， 用于复杂的线程同步
# 启动顺序很重要，要先wait，再notify
# 在调用with cond之后才能调用wait或者notify方法
# condithon有两层锁，一把底层锁会在线程调用了wait方法的时候释放，上面的锁会在每次调用wait的时候分配一把并放到cond的等待队列中，
#   等待notify方法的唤醒

import threading
class XiaoAi(threading.Thread):
    def __init__(self, cond):
        self.__answer_id = 0
        self.cond = cond
        super().__init__(name='xiaoai')
    def run(self) -> None:
        with self.cond:
            while True:
                if self.__answer_id >= 10:
                    break
                self.cond.wait()
                self.__answer_id += 1
                print('answer id = {}'.format(self.__answer_id))
                self.cond.notify()
        print('answer finished')

class TianMao(threading.Thread):
    def __init__(self, cond):
        self.__request_id = 0
        self.cond = cond
        super().__init__(name='tianmao')

    def run(self) -> None:
        with self.cond:
            while True:
                if self.__request_id >= 10:
                    break
                self.__request_id += 1
                print('requst id = {}'.format(self.__request_id))
                self.cond.notify()
                self.cond.wait()
        print('request finished')

if __name__ == '__main__':
    cond = threading.Condition()
    xiao_ai = XiaoAi(cond)
    tian_mao = TianMao(cond)

    # 天猫提问，小爱回答
    # 小爱先等待wait，天猫提问后notify小爱，然后等待wait小爱回答，小爱回答后并notify天猫
    xiao_ai.start()
    tian_mao.start()

    xiao_ai.join()
    tian_mao.join()
