import re

def getSortTitle(value):
    re.sub('^[Tt]he ', '', value)

def trimStart(needle, haystack):
    re.sub(f'^{needle}', '', haystack)
