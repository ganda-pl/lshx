help:
	@echo "Please provide one of the commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

coverage: ## run test suite with coverage reporting
	poetry run coverage run --source=. -m pytest .
	poetry run coverage report -m

test: ## run test suite
	poetry run pytest .

lint: ## run mypy
	poetry run mypy .
	poetry run flake8 .