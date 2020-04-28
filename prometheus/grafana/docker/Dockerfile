# docker build -t luanpeng/lp:grafana-6.0.0 .
FROM grafana/grafana:6.0.0
USER root
#RUN apt update && install -y git
#RUN cd /var/lib/grafana/plugins

# clickhouse数据源
Run grafana-cli plugins install vertamedia-clickhouse-datasource

# 时钟图
Run grafana-cli plugins install grafana-clock-panel
# 饼图
Run grafana-cli plugins install grafana-piechart-panel   
# 气泡图
Run grafana-cli plugins install digrich-bubblechart-panel
#RUN git clone https://github.com/grafana/piechart-panel.git
# 世界地图
Run grafana-cli plugins install raintank-worldping-app
# json数据
Run grafana-cli plugins install grafana-simple-json-datasource
#zabbix报警
Run grafana-cli plugins install alexanderzobnin-zabbix-app
# k8s监控应用
Run grafana-cli plugins install grafana-kubernetes-app
# WindRoseby 极坐标图
Run grafana-cli plugins install fatcloud-windrose-panel
# 雷达图
Run grafana-cli plugins install snuids-radar-panel
# 世界地图热力图
Run grafana-cli plugins install ovh-warp10-datasource
#　选点监控
Run grafana-cli plugins install natel-usgs-datasource
# es数据监控
Run grafana-cli plugins install stagemonitor-elasticsearch-app
# Plotly直接坐标系散点图
Run grafana-cli plugins install natel-plotly-panel
# 组织结构图
Run grafana-cli plugins install digiapulssi-organisations-panel
# ajax请求更新数据
Run grafana-cli plugins install ryantxu-ajax-panel


COPY clickhouse-grafana-master /var/lib/grafana/plugins