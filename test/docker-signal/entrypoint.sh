#!/bin/sh
# my test program
# 实际运行的工作程序
nohup python3.6 /data/server.py &
# 中断信号处理函数
prog_exit()
{
    echo begin-exit
    ps -ef| grep python |grep -v grep |awk '{print $2}'|xargs kill -15
}
# 注册中断处理函数
trap "prog_exit" 15

flag=1
# 水睡眠形式的主进程函数
while [ $flag -ne 0 ];do
    sleep 3;
    flag=`ps -ef| grep python |grep -v grep | wc -l`
done;
