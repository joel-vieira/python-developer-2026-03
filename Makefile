dev:
	make -j2 runserver assets

runserver:
	uv run python manage.py runserver

assets:
	npm run dev

lint-fix:
	uv run ruff check --fix .
	uv run ruff format .
	uv run djlint . --reformat

lint-check:
	uv run ruff check .
	uv run djlint . --lint
