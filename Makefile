.PHONY: setup-os
setup-os:
	sudo apt install python-pip
	sudo pip install -U pip pipenv

.PHONY: setup
setup:
	pipenv --rm || true
	pipenv --python python3.6
	pipenv install --dev

.PHONY: test
test:
	pipenv run pytest

.PHONY: check
check:
	pipenv run flake8
	pipenv run safety check

.PHONY: build
build: test check
	rm -rf dist
	pipenv run python setup.py sdist bdist_wheel

.PHONY: release
release: build
	pipenv run twine upload dist/* || true