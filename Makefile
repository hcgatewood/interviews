help: ## Print this help text
	@grep -Eh '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

reqs: ## Install requirements
	pip install -r requirements.txt

test: ## Run tests
	find . -mindepth 1 -maxdepth 1 -type d ! -name '.*' ! -name 'lib' -exec pytest {} \;
