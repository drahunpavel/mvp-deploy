# k8s manifests for MVP app

Manifests for deploying app components to k8s, including backend, frontend, database.

##  Composition

### 1. Backend
- auth-api-deployment.yml
- auth-api-service.yml
- ui-api-deployment.yml
- ui-api-service.yml

### 2. Frontend
- frontend-deployment.yml
- frontend-service.yml

### 3. Database
- postgres-deployment.yml
- postgres-service.yml
- postgres-pv.yml
- postgres-pvc.yml

### 4. Infrastructure
- namespace.yml
- storageclass-local.yml

## Deployment

```bash
kubectl apply -f namespace.yml

kubectl apply -f postgres-deployment.yml
kubectl apply -f postgres-service.yml

kubectl apply -f auth-api-deployment.yml
kubectl apply -f auth-api-service.yml

kubectl apply -f ui-api-deployment.yml
kubectl apply -f ui-api-service.yml

kubectl apply -f frontend-deployment.yml
kubectl apply -f frontend-service.yml
```