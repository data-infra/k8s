# docker build -t luanpeng/lp:hadoop-2.7.3-hbase-1.3.1-hive-2.3.4-spark-2.4.0-kelin-2.2.0 .
FROM luanpeng/lp:hadoop-2.7.3-2
# 安装hive
COPY apache-hive-2.3.4-bin /usr/local/hive
# 安装hbase
COPY hbase-1.3.1 /usr/local/hbase
# 安装spark
COPY spark-2.4.0 /usr/local/spark
# 安装kylin
COPY apache-kylin-2.4.1-bin-hbase1x /usr/local/kylin
# 添加mysql包
COPY mysql-connector-java-5.1.47-bin.jar /usr/local/hive/lib/
COPY mysql-connector-java-5.1.47-bin.jar /usr/local/hbase/lib/
COPY mysql-connector-java-5.1.47-bin.jar /usr/local/spark/lib/
COPY mysql-connector-java-5.1.47-bin.jar /usr/local/kylin/lib/





ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_HOME /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV LD_LIBRARY_PATH $HADOOP_HOME/lib/native/:$LD_LIBRARY_PATH
ENV HIVE_HOME /usr/local/hive
ENV HIVE_CONF $HIVE_HOME/conf
ENV HIVE_CONF_DIR $HIVE_HOME/conf
ENV HCAT_HOME $HIVE_HOME/hcatalog
ENV SPARK_HOME /usr/local/spark
ENV HADOOP_CLASSPATH $HADOOP_CLASSPATH:$HIVE_HOME/lib/*
ENV HBASE_HOME /usr/local/hbase
ENV KYLIN_HOME /usr/local/kylin
ENV PATH $PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin:$HIVE_HOME/bin:$HBASE_HOME/bin:$KYLIN_HOME/bin

WORKDIR /usr/local/kylin
EXPOSE 7070

# ENTRYPOINT ["sh", "-c", "/usr/local/kylin/bin/kylin.sh start; bash"]
