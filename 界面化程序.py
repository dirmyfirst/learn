#coding:gbk
import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title("Hello")
window.geometry("450x300")

#���ñ���
canvas = tk.Canvas(window,height = 450,width = 300)  #��������
image_file = tk.PhotoImage(file = 'xiao.gif') #����ͼƬ�ļ�
image = canvas.create_image(0,0,anchor = 'nw',image = image_file) #��ͼƬ���ڻ�����
canvas.pack(side = 'top') #���û���

#������ʾ��Ϣ
tk.Label(window,text = 'user name:').place(x = 50,y = 150)#��������λ��
tk.Label(window,text = 'password:').place(x = 50,y = 190)

#���������Ϣ
var_usr_name = tk.StringVar()#�������
var_usr_name.set('12345678901')#������ֵ
entry_usr_name = tk.Entry(window,textvariable = var_usr_name)#����entry��ʾ����
entry_usr_name.place(x = 160,y = 150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window,textvariable = var_usr_pwd,show = '*')#show��������Ϊ***
entry_usr_pwd.place(x = 160,y = 190)

#��¼����
def usr_login():
    usr_name = var_usr_name.get()#��¼��
    usr_pwd = var_usr_pwd.get()#��¼����
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info, usr_file)
            
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='��ӭ', message='����! ' + usr_name)
        else:
            tk.messagebox.showerror(message='������������µ�¼��')
    else:
         is_sign_up = tk.messagebox.askyesno('��ӭ','����û��ע�ᣬ��Ҫ����ע����?')
         if is_sign_up:
             usr_sign_up()      
def usr_sign_up():
    def sign_to_Mofan_Python():
        ##�������о��ǻ�ȡ����ע��ʱ���������Ϣ
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        ##�����Ǵ����Ǽ�¼���ݵ��ļ�����ע����Ϣ����
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)

        ##��������жϣ���������������벻һ�£�����ʾ`'Error', 'Password and confirm password must be the same!'`
        if np != npf:
            tk.messagebox.showerror('����', '��������������һ��!')

        ##����û����Ѿ������ǵ������ļ��У�����ʾ`'Error', 'The user has already signed up!'`
        elif nn in exist_usr_info:
            tk.messagebox.showerror('����', '���û����ѱ�ע��!')

        ##���������������ϴ�����ע���������Ϣ��¼���ļ����У�����ʾע��ɹ�`'Welcome', 'You have successfully signed up!'`
        ##Ȼ�����ٴ��ڡ�
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('��ϲ', '����ע��ɹ�!')
            ##Ȼ�����ٴ��ڡ�
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('ע�ᴰ��')
    new_name = tk.StringVar()#�������ע������ֵ������
    new_name.set('example@python.com')#�������ʾ��Ϊ'example@python.com'
    tk.Label(window_sign_up, text='�û�����').place(x=10, y= 10)#��`User name:`���������꣨10,10����
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)#����һ��ע������`entry`������Ϊ`new_name`
    entry_new_name.place(x=150, y=10)#`entry`���������꣨150,10��.
    
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='�û����룺').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='ȷ�����룺').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)
    
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='ע��', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)            

#��¼��Ϣ����
btn_login = tk.Button(window,text = '��¼',command = usr_login)
btn_login.place(x = 170,y = 230)
btn_sign_up = tk.Button(window,text = 'ע��',command = usr_sign_up)
btn_sign_up.place(x = 270,y = 230)


window.mainloop()
