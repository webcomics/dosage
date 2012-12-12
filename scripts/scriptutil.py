# Copyright (C) 2012 Bastian Kleineidam
import re


def contains_case_insensitive(adict, akey):
    for key in adict:
        if key.lower() == akey.lower():
            return True
    return False


_tagre = re.compile(r"<.+?>")
def remove_html_tags(text):
    return _tagre.sub("", text)


def capfirst(text):
    """Uppercase the first character of text."""
    if not text:
        return text
    return text[0].upper() + text[1:]


_ws = re.compile(r"\s+")
def compact_whitespace(text):
    if not text:
        return text
    return _ws.sub(" ", text)
