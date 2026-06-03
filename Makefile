run:
	uv run manage.py runserver
lint:
	uv run pre-commit run --all-files
#migrations commands
makemigrations:
	uv run manage.py makemigrations
migrate:
	uv run manage.py migrate
#superuser
createsuperuser:
	uv run manage.py createsuperuser
#fixture commands
save_post_fixture:
	$env:PYTHONUTF8 = "1"
	uv run manage.py dumpdata blog_app.Post --indent 2 --output fixtures/posts.json
load_post_fixture:
	uv run manage.py loaddata fixtures/posts.json
#custom commands
print_posts:
	uv run manage.py print_posts
print_published_posts:
	uv run manage.py print_published_posts
create_post:
	uv run manage.py create_post --author "${author}" --content "${content}" --title "${title}"
delete_post:
	uv run manage.py delete_post --post_id "${post_id}"
update_post_title:
	uv run manage.py update_post --post_id "${post_id}" --title "${title}"
