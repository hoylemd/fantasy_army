MAIN=farmy.py

all : go

go : $(MAIN)
	python $(MAIN)

test : clean tests
	nosetests -s --pdb

clean :
	rm -f *.pyc
	rm -f game/*.pyc
	rm -f farmy/*.pyc
	rm -f tests/*.pyc
	rm -f tests/test_farmy/*.pyc
	rm -f tests/test_game/*.pyc

