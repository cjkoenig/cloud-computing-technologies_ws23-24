# Introduction 

In this exercise, we will setup prometheus for the following tasks of the lab.

1. We use the blackbox module to monitor a web-host and the alarmmanager to send an alarm to telegram in case it is down (`blackbox.yml`, `custom_alerts.yml`, and `alertmanager.yml` )
2. We define jobs for prometheus to run periodically (`prometheus.yml`)
3. The monitored data is from prometheus itself, a host (`node-exporter`), the containers on a host (`cadvisor`), an nginx instance (`nginx-exporter`), the web application from lab1 (`web-app`), and a web host (`http-probe`). We will complete the setup in the following steps.


To send an alarm to telegram, you need to get a token from the [MiddlemanBot](https://t.me/MiddlemanBot).