import signal
import time

is_running = True

def sigint_handler(num, stack):
    print(num,stack)
    print('receive sigint')
    global is_running
    is_running = False

def sigterm_handler(num, stack):
    print(num,stack)
    print('receive sigterm')
    global is_running
    is_running = False

def main():
    signal.signal(signal.SIGINT, sigint_handler)
    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.siginterrupt(signal.SIGINT, False)
    signal.siginterrupt(signal.SIGTERM, False)

    while is_running:
        print('begin sleep')
        # 启动你的业务函数
        time.sleep(3)

    print("prepare exit")
    print("sleep 10")
    time.sleep(10)
    print("exit")
    

if __name__ == "__main__":
    main()
