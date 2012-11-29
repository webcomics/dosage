# Copyright (C) 2012 Bastian Kleineidam

def contains_case_insensitive(adict, akey):
    for key in adict:
        if key.lower() == akey.lower():
            return True
    return False

 
