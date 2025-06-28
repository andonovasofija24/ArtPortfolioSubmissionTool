# ArtPortfolioSubmissionTool

[GitHub Репозиториум](https://github.com/andonovasofija24/ArtPortfolioSubmissionTool)  
[Frontend Docker Image](https://hub.docker.com/r/andonovasofija24/art-portfolio-frontend)  
[Backend Docker Image](https://hub.docker.com/r/andonovasofija24/art-portfolio-backend)

---

## Преглед на проектот

Овој репозиториум содржи изворен код и конфигурации за деплојмент на Art Portfolio Submission Tool. Проектот ја опфаќа контеинеризацијата, оркестрацијата и CI/CD поставката за лесно и автоматизирано поставување на апликацијата.

---

## Барања и имплементација

| Барање                                                                                       | Локација / Опис на имплементација                                                                                                                                                    |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Апликацијата да ја поставите на јавен git репозиториум** (10%)                                | Овој репозиториум е јавен на GitHub: [ArtPortfolioSubmissionTool](https://github.com/andonovasofija24/ArtPortfolioSubmissionTool)                                                    |
| **Апликацијата да ја докеризирате** (10%)                                                        | Dockerfiles за frontend и backend се вклучени во проектот и се пуштени како слики (images) на Docker Hub:                                                                             |
|                                                                                              | - Frontend: [andonovasofija24/art-portfolio-frontend](https://hub.docker.com/r/andonovasofija24/art-portfolio-frontend)                                                                |
|                                                                                              | - Backend: [andonovasofija24/art-portfolio-backend](https://hub.docker.com/r/andonovasofija24/art-portfolio-backend)                                                                   |
| **Апликацијата и базата да ги оркестрирате со Docker Compose** (10%)                      | Фајл `docker-compose.yml` во коренот на проектот го оркестрира frontend, backend и база на податоци локално за развој и тестирање.                                                      |
| **Да изберете една CI платформа (GitHub Actions, GitLab CI, Jenkins, ...) и да сетирате pipeline за целосно CI или CI/CD решение: со push на git да се постави новата верзија на Docker имиџот на соодветен регистар (пр. на DockerHub).** (20%)                                                             | GitHub Actions workflows се конфигурирани во `.github/workflows/` за автоматско градење и пуштање на Docker images кон Docker Hub при push на гранки.                                 |
| **Да изработите Kubernetes манифести за следните работи:**                                                                    | Kubernetes манифести се во папката `manifests/` и ги опфаќаат следните компоненти:                                                                                                   |
| - Deployment за апликацијата со ConfigMaps/Secrets (10%)                                   | `manifests/deployment.yaml` ги дефинира Deployment-ите за frontend и backend со поврзани ConfigMaps и Secrets за конфигурација и креденцијали.                                         |
| - Service за апликацијата (10%)                                                             | `manifests/service.yaml` ги дефинира ClusterIP Service-ите кои ги изложуваат frontend и backend внатре во кластерот.                                                                  |
| - Ingress за апликацијата (10%)                                                             | `manifests/ingress.yaml` ја конфигурира Ingress ресурсот кој го насочува надворешниот сообраќај кон frontend сервисот преку NGINX ingress контролер.                                   |
| - StatefulSet за базата со ConfigMaps/Secrets (10%)                                        | `manifests/statefulset.yaml` го дефинира StatefulSet-от за базата на податоци (на пр. PostgreSQL) со volume claims, ConfigMaps и Secrets за креденцијали.                             |
| - Постави ги манифестите во посебен namespace и демонстрирај дека работи (10%)              | Сите Kubernetes манифести се поставени во одделен namespace `art-portfolio` за изолација на ресурсите, проверено со `kubectl get all -n art-portfolio`.                                |

---

## Како да користите

1. Клонирајте го репозиториумот:
   ```bash
   git clone https://github.com/andonovasofija24/ArtPortfolioSubmissionTool.git
   cd ArtPortfolioSubmissionTool
   
2. Користете Docker Compose за локален развој:
   ```bash
   docker-compose up --build
3. Deploy на Kubernetes кластер:
   ```bash
   kubectl apply -f manifests/ -n art-portfolio
4. Пристапете ја апликацијата преку конфигурираниот Ingress.

## Дополнителни информации
CI pipeline се активира при push на гранки и автоматски гради и пушта ажурирани Docker images.

Kubernetes манифестите вклучуваат добри практики за управување со secrets и конфигурации.

Проектот поддржува повеќе околини преку branches организација (dev, prod).