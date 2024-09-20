
all:
	cd sim/cs; make test
	cp README.md  index.md
	echo "## What\n\nThe simulation results can be seen in [sim/cs/README](sim/cs/README.html)" >> index.md
	pandoc --css pandoc.css -s index.md -o index.html
