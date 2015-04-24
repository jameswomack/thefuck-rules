scriptNames=$(shell ls rules | ag py$$)

all: readme

readme:
	echo "# The Fuck Scripts \n$(scriptNames)" > README.md
