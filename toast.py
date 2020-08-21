from win10toast import ToastNotifier
import time
import datetime
import threading


class Toast(object):

    def __init__(self, wish_time):
        self.wish_time = wish_time
        self.title = '1'
        self.msg = '2'
        self.toast = ToastNotifier()
        self.dt = datetime.datetime.now()
        self.now_time = self.dt.strftime('%Y-%m-%d %H:%M') # 取现在的时间点
        self.new_wish = self.wish() # 加上了年份的期望时间
    
    def wish(self):
        return time.strptime('{}-'.format(self.dt.strftime('%Y')) + self.wish_time , '%Y-%m-%d %H:%M')

    def toaster(self):    
        self.toast.show_toast(
            title= self.title,
            msg = self.msg,
            icon_path= 'one.ico',
            duration= 10,
            threaded=True)

    def no_time(self):     # 对比时间输出对应通知
        if self.now_time == str(self.new_wish):
            self.title = 'nihao'
            self.msg = '吃饭吗'

        else:
            self.title = '吃饭吗'
            self.msg = '黄焖鸡米饭'
        self.toaster()


if __name__ == '__main__':
    Toast('08-20 18:00').no_time()