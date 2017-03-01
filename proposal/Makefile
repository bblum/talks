.PHONY: clean

thesprop: thesprop.tex cmuthesis.cls citations.bib overview.tex quicksand.tex 410.tex pintos.tex tm.tex related.tex
	pdflatex $< ; bibtex $(<:%.tex=%) ; pdflatex $< ; pdflatex $<

clean:
	-rm -f *.aux *.log *.out
