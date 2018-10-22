venv: dev-requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur dev-requirements.txt
	touch venv

black: venv
	@status=$$(git status --porcelain pymagicc tests); \
	if test "x$${status}" = x; then \
		./venv/bin/black --exclude _version.py setup.py cite; \
	else \
		echo Not trying any formatting. Working directory is dirty ... >&2; \
	fi;

publish-on-pypi: venv
	-rm -rf build dist
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		./venv/bin/python setup.py bdist_wheel --universal; \
		./venv/bin/twine upload dist/*; \
	else \
		echo Working directory is dirty >&2; \
	fi;

test-pypi-install: venv
	$(eval TEMPVENV := $(shell mktemp -d))
	python3 -m venv $(TEMPVENV)
	$(TEMPVENV)/bin/pip install pip --upgrade
	$(TEMPVENV)/bin/pip install cite
	$(TEMPVENV)/bin/python -c "import sys; sys.path.remove(''); import cite; print(cite.__version__)"

flake8: venv
	./venv/bin/flake8 cite setup.py

.PHONY: flake8
