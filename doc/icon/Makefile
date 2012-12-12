ICOICONS := logo16x16.png logo32x32.png
ICNSICONS := logo16x16.png logo32x32.png logo48x48.png logo128x128.png

all:	favicon.ico favicon.icns

favicon.ico:	$(ICOICONS)
	png2ico favicon.ico $(ICOICONS)

favicon.icns:	$(ICNSICONS)
	png2icns favicon.icns $(ICNSICONS)
