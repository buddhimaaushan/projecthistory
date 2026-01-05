.PHONY: install test lint format api migrate clean

install:
	pip install -e .
	pip install -r requirements-dev.txt

test:
	pytest

api:
	uvicorn tempus.api.main:app --reload

migrate:
	alembic upgrade head

lint:
	ruff check tempus tests

format:
	ruff format tempus tests

clean:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	rm -rf build dist *.egg-info
