
all:
	cd sim/cs; make test
	pandoc --css pandoc.css -s README.md -o index.html
