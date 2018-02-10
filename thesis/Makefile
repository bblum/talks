.PHONY: clean

thesis: thesis.tex intro.tex overview.tex landslide.tex cmuthesis.cls citations.bib # quicksand.tex 410.tex pintos.tex tm.tex related.tex
	xelatex $< && bibtex $(<:%.tex=%) && xelatex $< && xelatex $< || true

clean:
	-rm -f *.aux *.log *.out
