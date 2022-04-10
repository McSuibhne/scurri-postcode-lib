import re

# Regex from: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
# Includes matching for special cases.
POSTCODE_REGEX = '^(([A-Z]{1,2}[0-9][A-Z0-9]' \
                 '?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ' \
                 '?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]' \
                 '?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'

COMP_REGEX = re.compile(POSTCODE_REGEX)

NON_GEOGRAPHIC_AREA_CODES = ("EC", "BS", "BT", "IM", "NE", "SA", "WV")


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
    if COMP_REGEX.match(postcode.upper().replace(" ", "").replace("-", "")):
        return True
    else:
        return False


def format_postcode(postcode: str) -> str:
    """
    Receives a valid UK postcode string
    and returns the code in standard format.
    Input: a UK postcode as a string.
    Output: a correctly formatted UK postcode
    as a string.
    """

    if validate_postcode(postcode) is False:
        raise InvalidPostcode()

    postcode = postcode.upper().replace(' ', '').replace('-', '')

    if len(postcode) == 3:
        # Handles non-geographic Special Cases
        return postcode
    elif len(postcode) == 4:
        if postcode[:2] in NON_GEOGRAPHIC_AREA_CODES:
            # Handles postcodes with no space
            return postcode
        else:
            # Handles Bermuda postcodes
            inward_code = postcode[-2:]
            outward_code = postcode[:-2]
            return outward_code + " " + inward_code
    elif postcode[-4:].isdigit():
        # Handles various British Overseas Territories
        inward_code = postcode[-4:]
        outward_code = postcode[:-4]
        return outward_code + "-" + inward_code
    else:
        # Handles post code formats where inward code is 3 characters long
        inward_code = postcode[-3:]
        outward_code = postcode[:-3]
        return outward_code + " " + inward_code
