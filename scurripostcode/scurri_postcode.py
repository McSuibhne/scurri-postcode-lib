import re

# Regex from: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
POSTCODE_REGEX = '^(([A-Z]{1,2}[0-9][A-Z0-9]' \
                            '?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ' \
                            '?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]' \
                            '?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'

COMPILED_REGEX = re.compile(POSTCODE_REGEX)


class InvalidPostcode(Exception):
    """Raised when an invalid code is
    passed to the format function"""
    pass


def validate_postcode(postcode: str) -> bool:
    """
    Determines whether a given string's
    characters are in valid UK postcode
    structure, regardless of format.
    Input: an unverified postcode as a string.
    Output: a boolean value.
    """
    if not COMPILED_REGEX.match(postcode.upper().replace(" ","").replace("-","")):
        return False
    else:
        return True


def format_postcode(postcode: str) -> str:
    """
    Receives a valid UK postcode string
    and returns the code in standard format.
    Input: a UK postcode as a string.
    Output: a correctly formatted UK postcode
    as a string.
    """

    if validate_postcode(postcode) == False:
        raise InvalidPostcode()

    postcode = postcode.upper().replace(' ', '').replace('-', '')

    inward_code = postcode[-3:]
    outward_code = postcode[:-3]

    return outward_code + " " + inward_code