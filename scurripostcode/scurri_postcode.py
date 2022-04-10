import re

# Regex from: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
POSTCODE_REGEX = '^(([A-Z]{1,2}[0-9][A-Z0-9]' \
                            '?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ' \
                            '?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]' \
                            '?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'

COMPILED_REGEX = re.compile(POSTCODE_REGEX)


def validate_postcode(postcode: str) -> bool:
    """
    Determines whether a given string's
    characters are in valid UK postcode
    structure, regardless of format.
    Input: an unverified postcode as a string.
    Output: a boolean.
    """
    if not COMPILED_REGEX.match(postcode.upper().replace(" ","").replace("-","")):
        return False
    else:
        return True

