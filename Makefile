isort:
	isort --recursive

flake8:
	flake8 . --ignore=E501,E722 --count --statistics

dev_install:
	pip3 install --upgrade pip
	pip3 install --pre -e .
	pip3 install -r dev-requirements.txt

sanity_check:
	pip3 list
test:
	pylint tap_dayforce --disable line-too-long,missing-module-docstring,invalid-name,missing-function-docstring,unused-argument,bare-except,useless-object-inheritance,no-member,missing-class-docstring,redefined-builtin,no-self-use
