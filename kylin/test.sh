MAX_SERVERS=3
server_str="kylin-0.kylin.cloudai-2.svc.cluster.local:7070"
for((i=1;i<${MAX_SERVERS};i++));
do
server_str="${server_str},kylin-${i}.kylin.cloudai-2.svc.cluster.local:7070"
echo $server_str
done
