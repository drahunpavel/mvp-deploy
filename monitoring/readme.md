# Kubernetes Monitoring

A set of manifests for the monitoring system in Kubernetes

##  Tools

- **Prometheus** — metrics collection
- **Grafana** — visualization of metrics
- **Blackbox-exporter / node-exporter / kube-state-metrics / cAdvisor** — sources of metrics

##  Deployment

```bash
kubectl apply -f ...

namespace.yml
cluster-role.yml

prometheus-config-map.yml
prometheus-deployment.yml
prometheus-service.yml

grafana-deployment.yml
grafana-service.yml

kube-state-metrics-deployment.yml
kube-state-metrics-service.yml

node-exporter-deployment.yml
node-exporter-service.yml

blackbox-config-map.yml
blackbox-deployment.yml
blackbox-service.yml
```