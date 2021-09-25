import re

def getSortTitle(value):

    return re.sub('^[Tt]he ', '', value)

def trimStart(needle, haystack):

    return re.sub(f'^{needle}', '', haystack)
