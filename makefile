FARMY_MAIN=farmy.py
SFLEET_MAIN=sfleet.py

MAIN=sfleet

sfleet: $(SFLEET_MAIN)
	python $(SFLEET_MAIN)

farmy : $(FARMY_MAIN)
	python $(FARMY_MAIN)

all : go

go: $(MAIN)

test : clean tests
	nosetests

debug-test: clean tests
	nosetests -s --pdb

clean :
	rm -f *.pyc
	rm -f game/*.pyc
	rm -f farmy/*.pyc
	rm -f tests/*.pyc
	rm -f tests/test_farmy/*.pyc
	rm -f tests/test_game/*.pyc

