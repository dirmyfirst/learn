#coding:gbk
import os,sys

def check_name(check_path,keyword):
    filelist = os.listdir(check_path)  # ����Ŀ¼�е��ļ�
    print(filelist)
    for text in filelist:              # ѭ���ļ��б�
        if ".txt" in text:             # ���˿��ܵ������ļ�, ֻ��ע
            txtfile = open(check_path+text)    # ƴ���ļ�·���������ļ�
            print(txtfile)
            for line in txtfile.readlines():    # ��ȡ�ļ�ÿһ�У���ѭ��
                if keyword in line:             # �ж��Ƿ��йؼ���������
                    print (line)
check_name("F:/pythonѧϰ/ѧϰ�ĵ�/","ѧϰ�ĵ�")


def checkname(open_name,save_name):
    export = ""
    for a,b,c in os.walk(open_name):
        export +="\n %s;%s;%s" % (a,b,c)
        open(save_name,'a').write(export)


#checkname("\pythonѧϰ\ѧϰ�ĵ�","test1.txt")
