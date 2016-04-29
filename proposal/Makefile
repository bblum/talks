.PHONY: clean

thesprop: thesprop.tex cmuthesis.cls citations.bib overview.tex
	pdflatex $< ; bibtex $(<:%.tex=%) ; pdflatex $< ; pdflatex $<

clean:
	-rm -f *.aux *.log *.out
