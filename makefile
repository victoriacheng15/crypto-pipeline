.PHONY: init format data delete


init:
	@pip install -r requirements.txt

format:
	@ruff format main.py utils

data:
	@python3 main.py data

delete:
	@python3 main.py delete