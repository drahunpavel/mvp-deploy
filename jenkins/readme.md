# Jenkins CI/CD Pipeline for k8s

Jenkins pipeline for building, publishing and deploying Docker images to a Kubernetes cluster. Includes Telegram notifications.

##  Requirements
- Jenkins with Pipeline plugin installed
- Jenkins agent
- Kubernetes cluster with token access
- Docker Hub 
- Telegram Bot for notifications

##  Jenkins Credentials

| ID                        | Тип               | 
|--------------------------|-------------------|
| `kubeconfig-template`    | File              |
| `K8S_TOKEN`              | String            |
| `K8S_CA_CERT`            | String            |
| `K8S_API_IP`             | String            |
| `env-auth-api`           | File              |
| `env-ui-api`             | File              |
| `env-db`                 | File              |
| `docker-hub-user-password` | Username/Password |
| `DOCKER_REGISTRY`        | String            |
| `TELEGRAM_BOT_TOKEN`     | String            |
| `TELEGRAM_BOT_CHAT_ID`   | String            | 

##  Pipeline Stages

### 1. Checkout Git
- Clones the repository

### 2. Prepare k8s
- Generates `kubeconfig` from template
- Checks access to cluster

### 3. Build Docker Images
- Builds images via `docker-compose.jenkins.yml`

### 4. Push Images
- Publishing images with the tag `${BUILD_TAG}`

### 5. Deploy to k8s
- Copies and modifies manifests
- Applies them to namespace

### 6. Telegram notification
- Sends a success or error message