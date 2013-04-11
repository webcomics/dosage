HOMEPAGE:=$(HOME)/public_html/dosage-webpage.git
WOK:=$(HOME)/projects/wok.git/wok

all:

comics:	../../testresults.txt
# regenerate comic pages
	rm -f content/comics/*.md
	env PYTHONPATH=../.. ./mkcomics.py $< content

votes:
	env PYTHONPATH=../.. ./mkvotes.py

media/favicon.ico:	../icon/favicon.ico
	cp $< $@

gen:	media/favicon.ico
# copy some static files
	cp ../dosage.1.html $(HOMEPAGE)
	env PYTHONPATH=$(HOME)/src $(WOK) -v

serve:
	xdg-open http://localhost:8080
	$(WOK) --server localhost:8080

upload:
	cd $(HOMEPAGE) && git add . && git commit -m "Updated" && git push

release: gen upload

.PHONY: all comics gen serve upload release votes
