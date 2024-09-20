


include ../../tech/make/sim.make

TB=tran
VIEW=Sch


test:
	${MAKE} typical summary

typical:
	cicsim run --name ${VIEW}_typical ${TB} ${OPT} ${VIEW} Gt Ktt Tt Vt

tfs:
	cicsim run --name ${VIEW}_tfs ${TB} ${OPT} ${VIEW} Gt "Ktt,Kff,Kss" Tt Vt

summary:
	cicsim summary --output "README.md"
	ls -1 output_tran/*.png | xargs -I{} echo  "![]({})\n" >> README.md
	echo  "\n\n# Testbench \n\n\`\`\`spice" >> README.md
	cat tran.spi >> README.md
	echo  "\n\`\`\` \n\n" >> README.md
	echo  "\n# Measurements \n\n\`\`\`spice" >> README.md
	cat tran.meas >> README.md
	echo  "\n\`\`\` \n\n" >> README.md
	echo  "\n# Post-Process \n\n\`\`\`python" >> README.md
	cat tran.py >> README.md
	echo  "\n\`\`\` \n\n" >> README.md
	pandoc --css ../../pandoc.css -s README.md -o README.html


clean:
	-rm -rf output_*
	-rm -rf __pycache__
	-rm *.run
	-rm *.pdf
	-rm *.csv
