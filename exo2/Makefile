all:
	docker compose up --build

clean:
	docker compose down

fclean:
	docker compose down --rmi all

purge:
	docker compose down -v

re: fclean all
