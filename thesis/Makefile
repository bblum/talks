.PHONY: clean

thesis: thesis.tex intro.tex background.tex landslide.tex cmuthesis.cls citations.bib # quicksand.tex 410.tex pintos.tex tm.tex related.tex
	xelatex $< ; bibtex $(<:%.tex=%) ; xelatex $< ; xelatex $<

clean:
	-rm -f *.aux *.log *.out
