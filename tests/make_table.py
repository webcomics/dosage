#!/usr/bin/python
import sys
import codecs

HTML_START = """<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="utf-8">
  <title>Dosage comic status</title>
</head>
<body>
"""

HTML_END = """
</body></html>
"""


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    filename = 'testresults.txt'
    with open(filename) as fp:
        tests = parse_test_data(fp)
    output = 'table.html'
    with codecs.open(output, 'w', 'utf-8') as fp:
        render_test_data(tests, fp)


def get_comic_name(line):
    return line.split('::')[1][4:]


def parse_test_data(fp):
    data = []
    for line in fp:
        if line.rstrip().endswith('::test_comic'):
            name = get_comic_name(line)
            failed = line.startswith('F')
            data.append((name, failed))
    data.sort()
    return data


def render_test_data(tests, fp):
    fp.write(HTML_START)
    fp.write('<table><th><td>Name</td><td>Status</td></th>\n')
    for name, failed in tests:
        status = failed and "broken" or "ok"
        fp.write('<tr><td>%s</td><td>%s</td></tr>\n' % (name, status))
    fp.write('</table>\n')
    fp.write(HTML_END)


if __name__ == '__main__':
    main()
