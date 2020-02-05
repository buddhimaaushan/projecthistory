.PHONY: install test lint format clean

install:
	pip install -e .
	pip install -r requirements-dev.txt

test:
	pytest

lint:
	flake8 tempus tests

format:
	black tempus tests

clean:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	rm -rf build dist *.egg-info
