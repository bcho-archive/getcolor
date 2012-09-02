.PHONY: clean-pyc clean

server:
	python wsgi/run.py

build_db:
	python wsgi/make_db.py

clean:  clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
