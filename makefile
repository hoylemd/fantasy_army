MAIN=farmy.py

all : go

go : $(MAIN)
	python $(MAIN)

test : clean tests
	nosetests --pdb tests

clean :
	rm -f *.pyc
	rm -f game/*.pyc
	rm -f farmy/*.pyc
	rm -f tests/*.pyc

