test:
	env/bin/python -m unittest test_solutions

shell:
	env/bin/python

solve:
	env/bin/python solutions/$(DAY)
