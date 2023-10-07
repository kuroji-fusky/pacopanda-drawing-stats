REQUIRED_NODE_VER := 19
REQUIRED_PYTHON_VER := 3.10

.PHONY: all clean

all:
	@echo "Setting up project"

	@if command -v node >/dev/null 2>&1; then \
		node_version=$$(node -v | cut -d "v" -f 2); \
		if [ "$${node_version%%.*}" -ge $(REQUIRED_NODE_VER) ]; then \
			yarn install; \
		else \
			echo "Error: Node.js version is less than $(REQUIRED_NODE_VER)"; \
			exit 1; \
		fi; \
	else \
		echo "Error: Node.js is not installed on your system"; \
		exit 1; \
	fi

	@if command -v python >/dev/null 2>&1; then \
		python_version=$$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))'); \
		if [ "$$(echo "$$python_version" | cut -d "." -f 1)" -eq 3 ] && [ "$$(echo "$$python_version" | cut -d "." -f 2)" -ge 10 ]; then \
			cd server && python -m venv venv && .\venv\Scripts\activate; \
		else \
			echo "Error: Python version is less than $(REQUIRED_PYTHON_VER)"; \
			exit 1; \
		fi; \
	else \
		echo "Error: Python is not installed "; \
		exit 1; \
	fi

clean:
	find . -type d -name "node_modules" -exec rm -rf {} +
	find . -type d -name ".next" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +
