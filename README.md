```py
1、上传
git init
git config --global user.name "名字"
git config --global user.email "邮箱"

git remote add origin git@github.com:yourName/yourRepo.git
(git remote add origin https://github.com/hanhailong/CustomRatingBar)

git add .(可以为具体文件)
git commit -m "代码提交"
上传github之前，要先pull一下，执行如下命令
git pull origin master
git push origin master

2、下载后上传
git clone https://github.com/xiangma/scrapy_spider.git
git add . （注：别忘记后面的.，此操作是把Test文件夹下面的文件都添加进来）
git commit -m “提交信息” （注：“提交信息”里面换成你需要，如“上传项目”）
git push -u origin master （注：此操作目的是把本地仓库push到github上面，此步骤需要你输入帐号和密码） 
```
