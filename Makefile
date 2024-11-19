install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall dist/*.whl
start:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --force-reinstall dist/*.whl
lint:
	poetry run flake8 gendiff
