start:
		docker-compose up
stop:
		docker-compose stop

db:
		docker-compose up -d
		docker-compose exec web pipenv run ./manage.py makemigrations
		docker-compose exec web pipenv run ./manage.py migrate
lint:
		docker-compose exec web pipenv run black product order
		docker-compose exec web pipenv run flake8 product order
		docker-compose exec web pipenv run isort product order
		docker-compose exec web pipenv run mypy product order
		docker-compose exec web pipenv run pylint product order