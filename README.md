# Docker Plus

Please download and unzip: https://cmder.app/

Please click on Cmder.exe to begin the terminal.

Task list: 

- [x] Create the basic application with FastAPI
- [x] Analyze the plan for tasks
- [x] Dockerfile and docker-compose files
- [x] A database service (preferably MariaDB)
- [x] Enhance main.py to read id of a person from MariaDB
- [x] configure init scripts for MariaDB
- [x] docker volume for mariadb service
- [x] docker volume for live coding on the main.py
- [x] api - connected to backend, database-connected to db
- [-] health checks for both the containers
- [x] separate environment variable files for different env (dev, prod)
- [ ] resource allocation for containers 
- [ ] scaling up as a feature
- [ ] hierarchical assimilation of compose files (maybe provide example with different resource allocations)
- [x] use alpine-based images in the dockerfile for reducing the attack surface
- [ ] multi-layer build (how to do it here?)
- [x] add nginx-based exercise for dockerfile and docker-compose