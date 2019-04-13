.PHONY: setup test

setup:
	@pip install -r requirements.txt

test:
	@nosetests -s
