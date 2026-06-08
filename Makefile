.PHONY: install test lint format type-check pre-commit-install clean build publish

# poetry
install:
	pip install poetry
	poetry install
add:
	poetry add $(name)
dev:
	poetry add --group dev $(name)
	
test:
	poetry run pytest tests/ -v

# ruff
lint:
	pip install ruff
	ruff check dj_reframe/

check_r:
	ruff check dj_reframe/

format:
	pip install ruff
	ruff format dj_reframe/
# mypy
type-check:
	pip install mypy
	mypy dj_reframe/
# pre-commit
pre-commit-install:
	pip install pre-commit
	pre-commit install

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +

build:
	poetry build

publish:
	poetry publish --build

check: lint type-check test
	@echo "All checks passed!"

setup: install pre-commit-install
	@echo "Development environment ready!"
