# Makefile

install:
	poetry install
	
build:
	poetry build
	
brain-games:
	poetry run brain-games
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 brain_games
