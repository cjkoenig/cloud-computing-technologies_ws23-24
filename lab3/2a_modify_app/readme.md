# Export Application Metrics to Prometheus

In this task, we will extend the app from lab1 to export the current value of the counter to prometheus.

1. Since our application bases on flask, we can use the exporter from [here](https://pypi.org/project/prometheus-flask-exporter/) and put it to the requirements.txt to have it available
2. We have to init the PrometheusMetrics object and decorate our application with @metrics calls
3. In our case, we do not want standard exports but only the value of the counter
4. Build and run the container as described in lab1, browse through http://localhost/metrics to check the output
5. Now your app is ready to be monitored by prometheus
