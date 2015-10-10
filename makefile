MAIN=farmy.py

all : go

go : $(MAIN)
	python $(MAIN)

test : tests
	nosetests --pdb tests

clean :
	rm *.pyc
	rm game/*.pyc
	rm tests/*.pyc`

