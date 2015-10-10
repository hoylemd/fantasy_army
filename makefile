all : go

go : asteroids.py
	python asteroids.py

test : tests
	nosetests --pdb tests

clean :
	rm *.pyc
	rm game/*.pyc
	rm tests/*.pyc`

