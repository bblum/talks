.PHONY: clean

thesis: thesis.tex background.tex cmuthesis.cls citations.bib # quicksand.tex 410.tex pintos.tex tm.tex related.tex
	pdflatex $< ; bibtex $(<:%.tex=%) ; pdflatex $< ; pdflatex $<

clean:
	-rm -f *.aux *.log *.out
