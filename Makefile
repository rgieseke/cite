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

flake8: venv
	./venv/bin/flake8 cite setup.py

.PHONY: flake8
