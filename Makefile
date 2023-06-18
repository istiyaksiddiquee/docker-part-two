ENV ?= dev

clean: 
	docker-compose -f docker-compose.yaml --env-file ./fast_api/env/.env.$(ENV) down

up:
	docker-compose -f docker-compose.yaml --env-file ./fast_api/env/.env.$(ENV) up --build