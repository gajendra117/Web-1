## ssh 外网访问

```
wan ip   100.64.4.220

ssh zhaozheng@100.64.4.220 -p 20002
```
在路由器上面绑定端口

## ip地址

实验室服务器的ip ：
192.168.3.87  ，用户名 zz

## ssh远程连接服务器 plt画图的问题

```
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot([1,2,3])
plt.savefig('myfig')
```

#scp -p 4588 remote@www.abc.com:/usr/local/sin.sh /home/administrator


## 获取远程服务器上的文件
scp -P 2223 root@10.23.185.16:/root/test.tar.gz /home/test.tar.gz

## 将本地文件上传到服务器上
scp -P 2223 /home/test.tar.gz root@10.23.185.16:/root/test.tar.gz