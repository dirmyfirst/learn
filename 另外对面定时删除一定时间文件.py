#coding:gbk
import os
import time
import datetime
from threading import Timer
import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title("ɾ������")
window.geometry("500x300")
t=tk.Text(window,height=4)
t.pack()

tk.Label(window,text = '����ɾ��·��:').place(x = 70,y = 158)
del_name = tk.StringVar()
del_name.set('E:\LTEMR���ߣ�SFTPDLL20171220)����')
entry_name = tk.Entry(window,textvariable = del_name,width = 35)
entry_name.place(x = 160,y = 160)        

#�ӽ����ȡ·��
def tk_file_path():
    del_file_path = del_name.get()
    return del_file_path
#��ȡ��ǰʱ���
def date():
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    return date
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
    log_file = open(date()[:10] + ".txt","a")
    for root,dirs,files in os.walk(file_path):
        for name in files:
            if name[-6:] == "001.gz":
                modify_time = TimeStampToTime(os.path.getmtime(os.path.join(root,name)))
                if modify_time[:10] < str(get_three_date()):
                    os.remove(os.path.join(root,name))
                    print (date() + "del file is:" + os.path.join(root,name))
                    log_file.write(date() + "del file is:" + os.path.join(root,name) + '\n')
                else:            
                    log_file.write(date() + os.path.join(root,name) +"this file didnot del��this file modify time is��"+ modify_time + "������ɾ��ʱ�����" + '\n')
    log_file.close()
#��ʱɾ��
def loop_del_file():
    print ("start del...")
    aa = tk.StringVar()
    aa.set(date() +'��ʼɾ������ǰ�ļ�...')
    kk = tk.Entry(window,textvariable = aa,width = 35)
    kk.place(x = 0,y = 0)
    del_files(tk_file_path())
    loop_time = Timer(5,loop_del_file)
    loop_time.start()
    print ("del Completed��")
    aa1 = tk.StringVar()
    aa1.set(date() + '����ǰ������ɾ����')
    kk1 = tk.Entry(window,textvariable = aa1,width = 35)
    kk1.place(x = 0,y = 20)
    
btn_login = tk.Button(window,text = '������ʼɾ��',command = loop_del_file)
btn_login.place(x = 200,y = 230)


window.mainloop()
