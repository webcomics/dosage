#!/usr/bin/python
# update languages.py from pycountry
import os
import codecs
import pycountry

basepath = os.path.dirname(os.path.dirname(__file__))

def main():
    """Update language information in dosagelib/languages.py."""
    fn =os.path.join(basepath, 'dosagelib', 'languages.py')
    encoding = 'utf-8'
    with codecs.open(fn, 'w', encoding) as f:
        f.write('# -*- coding: %s -*-%s' % (encoding, os.linesep))
        f.write('# ISO 693-1 language codes from pycountry%s' % os.linesep)
        write_languages(f)


def write_languages(f):
    """Write language information."""
    f.write("Iso2Language = {%s" % os.linesep)
    for language in pycountry.languages:
        if hasattr(language, 'alpha2'):
            f.write("    %r: %r,%s" % (language.alpha2, language.name, os.linesep))
    f.write("}%s" % os.linesep)


if __name__ == '__main__':
    main()
