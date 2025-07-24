.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

init_env: ## Initialize the environment
	@echo "Initializing environment..."
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt

run_all: ## Run the application
	@echo "Running the application..."
	$(MAKE) init_env
	source venv/bin/activate && uvicorn app.main:app --reload