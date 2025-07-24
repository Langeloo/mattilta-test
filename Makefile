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
	@echo "Iniciando servidor en background..."
	nohup venv/bin/uvicorn app.main:app --reload > uvicorn.log 2>&1 &

	@sleep 2
	@echo "Abriendo Swagger UI (/docs) y ReDoc (/redoc)..."
	@if command -v xdg-open >/dev/null 2>&1; then \
		xdg-open http://localhost:8000/docs; \
		xdg-open http://localhost:8000/redoc; \
	elif command -v open >/dev/null 2>&1; then \
		open http://localhost:8000/docs; \
		open http://localhost:8000/redoc; \
	else \
		echo "Servidor iniciado en http://localhost:8000"; \
		echo "Abre manualmente las URLs /docs y /redoc"; \
	fi

clear: ## Clear the environment
	@echo "Clearing the environment..."
	rm -rf venv
	rm -rf __pycache__
	find . -name "*.pyc" -exec rm -f {} \;
