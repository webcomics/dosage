MANFILES:=dosage.1.html

man:	$(MANFILES)

dosage.1.html: dosage.1
	man2html -r $< | tail -n +2 | sed 's/Time:.*//g' | sed 's@/:@/@g' > $@
#	patch --no-backup-if-mismatch --quiet $@ dosage.1.html.diff

.PHONY: all man
