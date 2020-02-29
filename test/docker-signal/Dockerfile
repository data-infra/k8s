# docker build -t test-signal .
FROM ubuntu:18.04

RUN apt-get update && \
  apt-get install -y python3.6 && \
  apt-get install -y golang-go && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

COPY ./demo.py /data/
COPY ./demo.go /data/
COPY ./demo.java /data/

COPY ./entrypoint.sh /data/

WORKDIR /data/

RUN javac demo.java
RUN go build demo.go

# 使用sh做优雅退出
# ENTRYPOINT ["/data/entrypoint.sh"]
# CMD ["bash"]

# 直接向python发起退出命令
# ENTRYPOINT ["python3.6","/data/demo.py"]

# 直接向jar包发起信号
ENTRYPOINT ["java","demo"]

# 直接向GO发起信号
# ENTRYPOINT [/data/demo"]



