#!/usr/bin/env python
import prometheus_client
from prometheus_client import Counter
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask

app = Flask(__name__)

requests_total = Counter("request_count", "Total request cout of the host")

# 如果只返回一个metrics
@app.route("/metrics")
def requests_count():
    requests_total.inc()
    # requests_total.inc(2)
    return Response(prometheus_client.generate_latest(requests_total),mimetype="text/plain")


# 如果返回多个metrics
#### 定义一个仓库，存放数据
REGISTRY = CollectorRegistry(auto_describe=False)
muxStatus = Gauge("mux_api_21","Api response stats is:",registry=REGISTRY)
manageStatus = Gauge("manage_api_21","Api response stats is:",registry=REGISTRY)

#### 定义路由
@app.route("/metrics")
def ApiResponse():
    muxStatus.set(muxCode)
    manageStatus.set(manageCode)
    return Response(prometheus_client.generate_latest(REGISTRY),mimetype="text/plain")


@app.route('/')
def index():
    requests_total.inc()
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
