PYTHON = python3

install:
	$(PYTHON) -m pip install --upgrade pip && \
	$(PYTHON) -m pip install -r requirements.txt

install_dev:
	$(PYTHON) -m pip install --upgrade pip && \
	$(PYTHON) -m pip install -r requirements-dev.txt && \
	$(PYTHON) -m pip install -r requirements.txt && \
	pre-commit install
