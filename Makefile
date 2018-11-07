SHELL = bash

lint:
	flake8 | tee >(wc -l)
	mypy --strict mkosi | tee >(wc -l)
