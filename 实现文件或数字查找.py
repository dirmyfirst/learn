#coding:gbk
import os,sys

def check_name(check_path,keyword):
    filelist = os.listdir(check_path)  # 搜索目录中的文件
    print(filelist)
    for text in filelist:              # 循环文件列表
        if ".txt" in text:             # 过滤可能的其它文件, 只关注
            txtfile = open(check_path+text)    # 拼合文件路径，并打开文件
            print(txtfile)
            for line in txtfile.readlines():    # 读取文件每一行，并循环
                if keyword in line:             # 判定是否有关键词在行中
                    print (line)
check_name("F:/python学习/学习文档/","学习文档")


def checkname(open_name,save_name):
    export = ""
    for a,b,c in os.walk(open_name):
        export +="\n %s;%s;%s" % (a,b,c)
        open(save_name,'a').write(export)


#checkname("\python学习\学习文档","test1.txt")
