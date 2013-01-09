# Copyright (C) 2012-2013 Bastian Kleineidam
import re
import json

def contains_case_insensitive(adict, akey):
    """Check if key is in adict. The search is case insensitive."""
    for key in adict:
        if key.lower() == akey.lower():
            return True
    return False


_tagre = re.compile(r"<.+?>")
def remove_html_tags(text):
    """Remove all HTML tags from text."""
    return _tagre.sub("", text)


def capfirst(text):
    """Uppercase the first character of text."""
    if not text:
        return text
    return text[0].upper() + text[1:]


_ws = re.compile(r"\s+")
def compact_whitespace(text):
    """Compact all subsequent whitespace to a single space."""
    if not text:
        return text
    return _ws.sub(" ", text)


def save_result(res, json_file):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def load_result(json_file):
    """Load contents of a json file."""
    with open(json_file, "rb") as f:
        return json.load(f)


def truncate_name(text):
    """Ensure the comic name does not exceed 100 characters."""
    return text[:100]
