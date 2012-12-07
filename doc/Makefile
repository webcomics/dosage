MANFILES:=dosage.1.html

all:	man testresults.html

man:	$(MANFILES)

dosage.1.html: dosage.1
	man2html -r $< | tail -n +2 | sed 's/Time:.*//g' | sed 's@/:@/@g' > $@
#	patch --no-backup-if-mismatch --quiet $@ dosage.1.html.diff

testresults.html:	../testresults.txt
	../scripts/mktestpage.py $< > $@

.PHONY: all man
