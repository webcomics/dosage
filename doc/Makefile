all:	dosage.1.html dosage.txt

dosage.txt: dosage.1
# make text file from man page for Windows builds
	cols=`stty size | cut -d" " -f2`; stty cols 72; man -l $< | sed -e 's/.\cH//g' > $@; stty cols $$cols

dosage.1.html: dosage.1
	man2html -r $< | tail -n +2 | sed 's/Time:.*//g' | sed 's@/:@/@g' > $@
	patch --no-backup-if-mismatch --quiet $@ dosage.1.html.diff

.PHONY: all
