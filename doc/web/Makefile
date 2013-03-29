HOMEPAGE:=$(HOME)/public_html/dosage-webpage.git
WOK:=$(HOME)/projects/wok.git/wok

all:

comics:	../../testresults.txt
# copy some static files
	cp ../dosage.1.html ../icon/favicon.ico $(HOMEPAGE)
# regenerate comic pages
	rm -f content/comics/*.md
	env PYTHONPATH=../.. ./mkcomics.py $< content

gen:
	$(WOK) -v

serve:
	xdg-open http://localhost:8080
	$(WOK) --server localhost:8080

upload:
	cd $(HOMEPAGE) && git add . && git commit -m "Updated" && git push

release: comics gen upload

.PHONY: all comics gen serve upload release
