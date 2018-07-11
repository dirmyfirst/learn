#coding:gbk
import os
import time
import datetime

start = time.clock()
fib =lambda n,x=0,y=1:x if not n else fib(n-1,y,x+y)
#保存操作日志
log_file = open("log_file.txt","a")
#获取当前时间点
date = time.strftime("%Y-%m-%d %H:%M:%S")
#获取文件修改时间点
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
#获取3天前的日期
def get_three_date():
    today = datetime.date.today()
    three_day_ago = today - datetime.timedelta(days=3)
    return three_day_ago
#判断当前文件是否为3天前文件，如果是，则删除
def del_files(file_path):
    for root,dirs,files in os.walk(file_path):
        for name in files:
            if name[-6:] == "001.gz":
                modify_time = TimeStampToTime(os.path.getmtime(os.path.join(root,name)))
                if modify_time[:10] < str(get_three_date()):
                    os.remove(os.path.join(root,name))
                    print date + "删除的文件是:" + os.path.join(root,name)
                    log_file.write(date + "删除的文件是:" + os.path.join(root,name) + '\n')
                else:
                    print date + os.path.join(root,name) + "该文件不可以删除，该文件最近修改时间为："+ modify_time + "，不在删除时间段内"
                    log_file.write(date + os.path.join(root,name) +"该文件不可以删除，该文件最近修改时间为："+ modify_time + "，不在删除时间段内" + '\n')
    log_file.close()
end = time.clock()

if __name__ == "__main__":
    del_file_path = "E:\2017年工作记录"
    del_files(del_file_path)
    print ("read: %f s" % (end - start))
