run:
	uv run manage.py runserver
lint:
	uv run pre-commit run --all-files
makemigrations:
	uv run manage.py makemigrations
migrate:
	uv run manage.py migrate
createsuperuser:
	uv run manage.py createsuperuser
