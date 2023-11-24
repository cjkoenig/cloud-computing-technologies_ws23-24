# Monitor an nginx Instance 

Now we prepare an nginx instance to be monitored by prometheus.

1. nginx has an integrated module that provides some basic data: [ngx_http_stub_status_module](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html#stub_status)
2. It is (usually) enabled by default and we only need to put an additional listener to the config (see nginx-prometheus.conf) and mount it into the container
3. For prometheus, we need an exporter that is transforms the data to the correct format. We use the [nginx-prometheus-exporter](https://github.com/nginxinc/nginx-prometheus-exporter)
