# Deployment Guide

## Overview
Hướng dẫn triển khai MLOps system lên các môi trường khác nhau, bao gồm local development, staging và production.

## Prerequisites

### System Requirements
- CPU: 4+ cores
- RAM: 8GB+
- Storage: 50GB+
- OS: Linux (Ubuntu 20.04+), macOS, Windows 10+

### Software Requirements
- Docker 20.10+
- Docker Compose 2.0+
- Kubernetes 1.20+
- kubectl 1.20+
- Helm 3.0+
- Python 3.9+
- Git

### Cloud Requirements
- Cloud provider account (AWS, GCP, Azure)
- Container registry access
- Kubernetes cluster
- Storage service
- Database service

## Local Deployment

### Docker Compose
1. Build images:
```bash
docker-compose build
```

2. Start services:
```bash
docker-compose up -d
```

3. Check status:
```bash
docker-compose ps
```

4. View logs:
```bash
docker-compose logs -f
```

### Local Kubernetes
1. Start local cluster:
```bash
minikube start
```

2. Deploy application:
```bash
kubectl apply -f deployment/kubernetes/local/
```

3. Check deployment:
```bash
kubectl get pods
kubectl get services
```

## Cloud Deployment

### AWS Deployment

#### EKS Setup
1. Create EKS cluster:
```bash
eksctl create cluster \
  --name mlops-cluster \
  --region us-west-2 \
  --node-type t3.large \
  --nodes 3
```

2. Configure kubectl:
```bash
aws eks update-kubeconfig --name mlops-cluster --region us-west-2
```

#### ECR Setup
1. Create repository:
```bash
aws ecr create-repository --repository-name mlops-api
```

2. Push images:
```bash
aws ecr get-login-password | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
docker tag mlops-api:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/mlops-api:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/mlops-api:latest
```

#### Deployment
1. Create namespace:
```bash
kubectl create namespace mlops
```

2. Deploy application:
```bash
kubectl apply -f deployment/kubernetes/aws/
```

3. Configure ingress:
```bash
kubectl apply -f deployment/kubernetes/aws/ingress.yaml
```

### GCP Deployment

#### GKE Setup
1. Create GKE cluster:
```bash
gcloud container clusters create mlops-cluster \
  --zone us-central1-a \
  --machine-type e2-standard-4 \
  --num-nodes 3
```

2. Configure kubectl:
```bash
gcloud container clusters get-credentials mlops-cluster --zone us-central1-a
```

#### GCR Setup
1. Configure Docker:
```bash
gcloud auth configure-docker
```

2. Push images:
```bash
docker tag mlops-api:latest gcr.io/$PROJECT_ID/mlops-api:latest
docker push gcr.io/$PROJECT_ID/mlops-api:latest
```

#### Deployment
1. Create namespace:
```bash
kubectl create namespace mlops
```

2. Deploy application:
```bash
kubectl apply -f deployment/kubernetes/gcp/
```

3. Configure ingress:
```bash
kubectl apply -f deployment/kubernetes/gcp/ingress.yaml
```

### Azure Deployment

#### AKS Setup
1. Create AKS cluster:
```bash
az aks create \
  --resource-group mlops-rg \
  --name mlops-cluster \
  --node-count 3 \
  --node-vm-size Standard_D4s_v3
```

2. Configure kubectl:
```bash
az aks get-credentials --resource-group mlops-rg --name mlops-cluster
```

#### ACR Setup
1. Create registry:
```bash
az acr create --resource-group mlops-rg --name mlopsregistry --sku Basic
```

2. Push images:
```bash
az acr login --name mlopsregistry
docker tag mlops-api:latest mlopsregistry.azurecr.io/mlops-api:latest
docker push mlopsregistry.azurecr.io/mlops-api:latest
```

#### Deployment
1. Create namespace:
```bash
kubectl create namespace mlops
```

2. Deploy application:
```bash
kubectl apply -f deployment/kubernetes/azure/
```

3. Configure ingress:
```bash
kubectl apply -f deployment/kubernetes/azure/ingress.yaml
```

## Configuration Management

### Environment Variables
1. Create `.env` file:
```bash
cp .env.example .env
```

2. Update variables:
```bash
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mlops
DB_USER=admin
DB_PASSWORD=secret

# API
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# Monitoring
PROMETHEUS_HOST=localhost
PROMETHEUS_PORT=9090
GRAFANA_HOST=localhost
GRAFANA_PORT=3000
```

### Secrets Management
1. Create secrets:
```bash
kubectl create secret generic mlops-secrets \
  --from-literal=db-password=secret \
  --from-literal=api-key=key123 \
  --namespace mlops
```

2. Use secrets in deployment:
```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: mlops-secrets
        key: db-password
```

## Monitoring Setup

### Prometheus
1. Install Prometheus:
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack
```

2. Configure scraping:
```yaml
scrape_configs:
  - job_name: 'mlops-api'
    static_configs:
      - targets: ['mlops-api:8000']
```

### Grafana
1. Install Grafana:
```bash
helm install grafana grafana/grafana
```

2. Import dashboards:
```bash
kubectl create configmap grafana-dashboards \
  --from-file=monitoring/grafana/dashboards/
```

## Backup & Recovery

### Database Backup
1. Configure backup:
```yaml
backup:
  schedule: "0 0 * * *"
  retention:
    days: 7
  storage:
    type: "s3"
    bucket: "mlops-backups"
```

2. Run backup:
```bash
kubectl create job --from=cronjob/backup-db manual-backup
```

### Model Backup
1. Configure backup:
```yaml
backup:
  schedule: "0 */6 * * *"
  retention:
    versions: 10
  storage:
    type: "s3"
    bucket: "mlops-backups"
```

2. Run backup:
```bash
kubectl create job --from=cronjob/backup-model manual-backup
```

## Scaling

### Horizontal Scaling
1. Configure HPA:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: mlops-api
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: mlops-api
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

2. Apply configuration:
```bash
kubectl apply -f deployment/kubernetes/hpa.yaml
```

### Vertical Scaling
1. Configure VPA:
```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: mlops-api
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: mlops-api
  updatePolicy:
    updateMode: "Auto"
```

2. Apply configuration:
```bash
kubectl apply -f deployment/kubernetes/vpa.yaml
```

## Troubleshooting

### Common Issues
1. **Pod CrashLoopBackOff**
   - Check logs: `kubectl logs <pod-name>`
   - Check events: `kubectl describe pod <pod-name>`
   - Check configuration: `kubectl get configmap <config-name> -o yaml`

2. **Service Unavailable**
   - Check service: `kubectl describe service <service-name>`
   - Check endpoints: `kubectl get endpoints <service-name>`
   - Check network policy: `kubectl get networkpolicy`

3. **Resource Issues**
   - Check resource usage: `kubectl top pods`
   - Check node capacity: `kubectl describe node`
   - Check resource limits: `kubectl get deployment <deployment-name> -o yaml`

### Debugging Tools
1. **kubectl debug**
```bash
kubectl debug <pod-name> -it --image=busybox
```

2. **kubectl exec**
```bash
kubectl exec -it <pod-name> -- /bin/bash
```

3. **kubectl port-forward**
```bash
kubectl port-forward <pod-name> 8000:8000
```

## Maintenance

### Updates
1. Update images:
```bash
kubectl set image deployment/mlops-api mlops-api=mlops-api:new-version
```

2. Rollback:
```bash
kubectl rollout undo deployment/mlops-api
```

### Cleanup
1. Remove resources:
```bash
kubectl delete -f deployment/kubernetes/
```

2. Remove namespace:
```bash
kubectl delete namespace mlops
```

## Security

### Network Policies
1. Configure policy:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: mlops-api-policy
spec:
  podSelector:
    matchLabels:
      app: mlops-api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8000
```

2. Apply policy:
```bash
kubectl apply -f deployment/kubernetes/network-policy.yaml
```

### RBAC
1. Configure roles:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: mlops-api-role
rules:
- apiGroups: [""]
  resources: ["pods", "services"]
  verbs: ["get", "list", "watch"]
```

2. Apply roles:
```bash
kubectl apply -f deployment/kubernetes/rbac.yaml
```

## Best Practices

### Deployment
- Use rolling updates
- Implement health checks
- Configure resource limits
- Use secrets for sensitive data
- Implement proper logging

### Monitoring
- Set up proper metrics
- Configure alerts
- Monitor resource usage
- Track application performance
- Monitor security events

### Security
- Use network policies
- Implement RBAC
- Regular security updates
- Encrypt sensitive data
- Regular security audits

### Backup
- Regular backups
- Test restore procedures
- Multiple backup locations
- Version control
- Disaster recovery plan 