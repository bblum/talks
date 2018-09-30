.PHONY: clean

thesis: thesis.tex intro.tex overview.tex landslide.tex quicksand.tex education.tex tm.tex related.tex future.tex cmuthesis.cls citations.bib
	xelatex $< && bibtex $(<:%.tex=%) && xelatex $< && xelatex $< || true

clean:
	-rm -f *.aux *.log *.out
