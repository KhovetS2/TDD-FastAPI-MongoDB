
run:
	@fastapi dev ./store/main.py

precommit-install:
	@poetry run pre-commit install
