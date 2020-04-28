kubectl create ns monitoring
kubectl create -f ./operator/operator-sa.yml
kubectl create -f ./operator/operator-rbac.yml 
kubectl create -f ./operator/operator-svc.yml
kubectl create -f ./operator/operator-dp.yml
kubectl create -f ./alertmanater/alertmanager-main-sa.yml       # 创建alert的配置文件，定义报警方式
kubectl create -f ./alertmanater/alertmanager-main-secret.yml
kubectl create -f ./alertmanater/alertmanager-main-svc.yml
kubectl create -f ./alertmanater/alertmanager-main.yml
kubectl create -f ./node-exporter/node-exporter-sa.yml
kubectl create -f ./node-exporter/node-exporter-rbac.yml
kubectl create -f ./node-exporter/node-exporter-svc.yml
kubectl create -f ./node-exporter/node-exporter-ds.yml
kubectl create -f ./kube-state-metrics/kube-state-metrics-sa.yml
kubectl create -f ./kube-state-metrics/kube-state-metrics-rbac.yml
kubectl create -f ./kube-state-metrics/kube-state-metrics-svc.yml
kubectl create -f ./kube-state-metrics/kube-state-metrics-dp.yml
kubectl create -f ./grafana/grafana-sa.yml
kubectl create -f ./grafana/grafana-source.yml                # 自定义配置文件，定义显示方式
kubectl create -f ./grafana/grafana-datasources.yml
kubectl create -f ./grafana/grafana-admin-secret.yml
kubectl create -f ./grafana/grafana-svc.yml
kubectl create -f ./grafana/pv-pvc-hostpath.yml
kubectl create configmap grafana-config --from-file=./grafana/defaults.ini --namespace=monitoring  # 创建配置conifgmap
kubectl create -f ./grafana/grafana-dp.yml
kubectl create -f ./service-discovery/kube-controller-manager-svc.yml
kubectl create -f ./service-discovery/kube-scheduler-svc.yml
kubectl create -f ./pushgateway/pushgateway-serviceaccount.yaml
kubectl create -f ./pushgateway/pushgateway-service.yaml
kubectl create -f ./pushgateway/pushgateway-deployment.yaml
kubectl create -f ./prometheus/prometheus-main.yml          # prometheus-operator  部署成功后才能创建成功  会创建自定义类型，需要执行两遍,# 部署后记得修改数据的保留时长，启动参数"--storage.tsdb.retention=15d",
kubectl create -f ./prometheus/prometheus-rules.yml              # 自定义配置文件，定义收集和报警规则    不要使用pvc，大了容易报错
kubectl create -f ./prometheus/prometheus-sa.yml
kubectl create -f ./prometheus/prometheus-rbac.yml
kubectl create -f ./prometheus/prometheus-svc.yml

kubectl create -f ./servicemonitor/alertmanager-sm.yml
kubectl create -f ./servicemonitor/coredns-sm.yml
kubectl create -f ./servicemonitor/kube-apiserver-sm.yml
kubectl create -f ./servicemonitor/kube-controller-manager-sm.yml
kubectl create -f ./servicemonitor/kube-scheduler-sm.yml
kubectl create -f ./servicemonitor/kubelet-sm.yml             # 请先确保每个节点的kubelet 添加了authentication-token-webhook=true和authorization-mode=Webhook参数
kubectl create -f ./servicemonitor/kubestate-metrics-sm.yml    # lable必须是k8s-app  因为prometheus是按这个查找的。不然prometheus采集不了该资源
kubectl create -f ./servicemonitor/node-exporter-sm.yml
kubectl create -f ./servicemonitor/prometheus-operator-sm.yml
kubectl create -f ./servicemonitor/prometheus-sm.yml
kubectl create -f ./servicemonitor/pushgateway-sm.yml
