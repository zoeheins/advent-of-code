test:
	env/bin/python -m unittest test_solutions

solve:
	env/bin/python solutions/$(DAY)

env:
	python3 -m venv env

shell:
	python3 -m bpython
