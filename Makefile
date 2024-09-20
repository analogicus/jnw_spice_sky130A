
all:
	cd sim/cs; make test
	echo "# JNW_SPICE_SKY130A" > index.md
	echo "## What\n\nThe simulation results can be seen in [sim/cs/README](sim/cs/README.html)" >> index.md
	cat README.md >> index.md

	pandoc --css pandoc.css -s index.md -o index.html
