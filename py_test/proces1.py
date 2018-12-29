import multiprocessing
import os,signal

import time

process_pid_list = []
def job(n):
    pid = os.getpid()
    print('成功创建第%s个子进程，当前子进程pid：%s' %(n, pid))
    # while 1:
    #     print("第 %s 个进程 pid：%s 正在运行........" %(n, pid))
    #     time.sleep(2)

def create_process():
    num = int(input("请输入要创建进程数量："))
    for i in range(num):
        p = multiprocessing.Process(target=job,args=(i+1,))
        p.start()
        process_pid_list.append(p.pid)


def print_process():
    for pid in process_pid_list:
        print("child pid：%s" %pid)

def kill_one_process(n):
    if int(n) > len(process_pid_list):
        print("too more！")
        time.sleep(2)
    else:
        pid = process_pid_list[int(n) - 1]
        # cmd = 'kill ' + str(pid)
        try:
            # os.system(cmd)
            os.kill(pid,signal.SIGILL)
            # no jiang shi jincheng
            signal.signal(signal.SIGCHLD,signal.SIG_IGN)
        except:
            print("你创建的进程 pid：%s 已经不存在了" %pid)
        else:
            print("正在kill你创建的第%s个进程 pid：%s!" %(n,pid))

def kill_all_process():
    print("****************want to kill all！***************")
    for pid in process_pid_list:
        # cmd = 'kill ' + str(pid)
        try:
            # os.system(cmd)
            os.kill(pid,signal.SIGKILL)
        except:

            print("你选择要kill的进程 pid：%s 已经不存在了" % pid)
        else:
            print("正在kill你创建的进程 pid：%s......" % pid)
    print("***************已经杀死所有子进程！*****************")

if __name__ == "__main__":
    create_process()
    print_process()
    print(process_pid_list)
    # 死循环，输入子进程的序号（非pid）来kill对应的进程，q退出死循环。
    while 1:
        n = input()
        if n == 'q':
            break
        elif n.isdigit():
            kill_one_process(n)
        else:
            print("请正确输入！")

    kill_all_process()