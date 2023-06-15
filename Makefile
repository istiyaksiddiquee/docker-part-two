
up: 
	docker compose -f docker-compose.yaml --env-file .\fast_api\env\.env.prod up

clean:
	docker compose -f docker-compose.yaml --env-file .\fast_api\env\.env.prod down