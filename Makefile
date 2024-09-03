PATH_TO_FILE := main.py
APP_NAME := app

build:
	docker compose build

run: build
	docker compose run -e PATH_TO_FILE=$(PATH_TO_FILE) $(APP_NAME)

stop:
	docker compose down

clean:
	docker compose down --rmi all --volumes --remove-orphans

.PHONY: build run stop clean
