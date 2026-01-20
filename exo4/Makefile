COMPOSE=docker compose

.PHONY: purge-bdd purge-all up down

purge-bdd:
	$(COMPOSE) down -v
	docker volume prune -f

purge-all:
	$(COMPOSE) down -v --rmi all --remove-orphans
	docker volume prune -f
	docker network prune -f
	$(COMPOSE) up -d --build

up:
	$(COMPOSE) up -d --build

down:
	$(COMPOSE) down
