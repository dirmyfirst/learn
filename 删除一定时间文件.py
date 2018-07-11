#coding:gbk
import os
import time
import datetime

start = time.clock()
fib =lambda n,x=0,y=1:x if not n else fib(n-1,y,x+y)
#���������־
log_file = open("log_file.txt","a")
#��ȡ��ǰʱ���
date = time.strftime("%Y-%m-%d %H:%M:%S")
#��ȡ�ļ��޸�ʱ���
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
#��ȡ3��ǰ������
def get_three_date():
    today = datetime.date.today()
    three_day_ago = today - datetime.timedelta(days=3)
    return three_day_ago
#�жϵ�ǰ�ļ��Ƿ�Ϊ3��ǰ�ļ�������ǣ���ɾ��
def del_files(file_path):
    for root,dirs,files in os.walk(file_path):
        for name in files:
            if name[-6:] == "001.gz":
                modify_time = TimeStampToTime(os.path.getmtime(os.path.join(root,name)))
                if modify_time[:10] < str(get_three_date()):
                    os.remove(os.path.join(root,name))
                    print date + "ɾ�����ļ���:" + os.path.join(root,name)
                    log_file.write(date + "ɾ�����ļ���:" + os.path.join(root,name) + '\n')
                else:
                    print date + os.path.join(root,name) + "���ļ�������ɾ�������ļ�����޸�ʱ��Ϊ��"+ modify_time + "������ɾ��ʱ�����"
                    log_file.write(date + os.path.join(root,name) +"���ļ�������ɾ�������ļ�����޸�ʱ��Ϊ��"+ modify_time + "������ɾ��ʱ�����" + '\n')
    log_file.close()
end = time.clock()

if __name__ == "__main__":
    del_file_path = "E:\2017�깤����¼"
    del_files(del_file_path)
    print ("read: %f s" % (end - start))
