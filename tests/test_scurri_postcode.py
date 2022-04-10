import unittest
from scurripostcode import scurri_postcode

GOOD_STANDARD_CODES = ["EC1A 1BB",
                       "W1A 0AX",
                       "M1 1AE",
                       "B33 8TH",
                       "CR2 6XH",
                       "DN55 1PT",
                       "BS16 9HW"]

BAD_FORMAT_CODES = ["EC1A   1B B",
                    "  W1A 0 AX  ",
                    "M  1 1A E ",
                    "B338TH",
                    "C  R 2 6 X H",
                    "DN551     PT",
                    "BS16 9H-W"]

GOOD_SPECIAL_POSTCODES = ["AI-2640",
                          "KY1-1602",
                          "MSR-1330",
                          "VG-1140",
                          "CR 03",
                          "GE CX",
                          "BS98"]

BAD_FORMAT_SPECIAL_CODES = [" AI         2640  ",
                            "KY1-16 02 ",
                            "MSR1330   ",
                            "V G 1 1 4 0",
                            "C-R 0 3",
                            "GEC  X",
                            "BS98"]

INVALID_OUTWARD_CODES = ["ECRA 1BB",
                         "WA 0AX",
                         "M 1AE",
                         "333 8TH",
                         "9R2 6XH",
                         "DN5AA 1PT"
                         "9HW"]

INVALID_INWARD_CODES = ["EC1A BB",
                        "W1A ",
                        "M1 1E",
                        "B33 87H",
                        "CR2 6XNH",
                        "DN55 1PT0"
                        "BS16 9"]

INVALID_CHARACTER_CODES = ["EC1A@1BB",
                           "W1A|1AX",
                           "",
                           "B33$8TH",
                           "CR2 =6XH",
                           "DN55 .1PT"]


class TestPostcodeValidation(unittest.TestCase):
    """Test cases for scurri_postcode.validate_postcode()
       Tests acceptance of both standard and special valid
       codes, rejection of invalid codes"""

    def test_uppercase_valid_codes(self):
        for postcode in GOOD_STANDARD_CODES:
            self.assertTrue(
                scurri_postcode.validate_postcode(postcode),
                postcode)

    def test_lowercase_valid_codes(self):
        for postcode in GOOD_STANDARD_CODES:
            self.assertTrue(
                scurri_postcode.validate_postcode(postcode.lower()),
                postcode)

    def test_poorly_formatted_valid_codes(self):
        for postcode in BAD_FORMAT_CODES:
            self.assertTrue(
                scurri_postcode.validate_postcode(postcode),
                postcode)

    def test_special_cases_valid_codes(self):
        for postcode in GOOD_SPECIAL_POSTCODES:
            self.assertTrue(
                scurri_postcode.validate_postcode(postcode),
                postcode)

    def test_invalid_outward_codes(self):
        for postcode in INVALID_OUTWARD_CODES:
            self.assertFalse(
                scurri_postcode.validate_postcode(postcode),
                postcode)

    def test_invalid_inward_codes(self):
        for postcode in INVALID_INWARD_CODES:
            self.assertFalse(
                scurri_postcode.validate_postcode(postcode),
                postcode)

    def test_invalid_characters_codes(self):
        for postcode in INVALID_CHARACTER_CODES:
            self.assertFalse(
                scurri_postcode.validate_postcode(postcode),
                postcode)


class TestPostcodeFormatting(unittest.TestCase):
    """Test cases for scurri_postcode.format_postcode()
       Tests correct formatting of both standard and
       special valid codes, each with both correct and
       bad formatting on submission. Also tests rejection
       of invalid codes through raising a custom exception"""

    def test_uppercase_valid_codes_formatting(self):
        for postcode in GOOD_STANDARD_CODES:
            self.assertEqual(
                scurri_postcode.format_postcode(postcode),
                postcode)

    def test_lowercase_valid_codes_formatting(self):
        for postcode in GOOD_STANDARD_CODES:
            self.assertEqual(
                scurri_postcode.format_postcode(postcode.lower()),
                postcode)

    def test_poorly_formatted_valid_codes_formatting(self):
        for i in range(0, len(BAD_FORMAT_CODES)):
            self.assertEqual(
                scurri_postcode.format_postcode(BAD_FORMAT_CODES[i]),
                GOOD_STANDARD_CODES[i])

    def test_special_cases_valid_codes_formatting(self):
        for postcode in GOOD_SPECIAL_POSTCODES:
            self.assertTrue(
                scurri_postcode.validate_postcode(postcode),
                postcode)

    def test_poorly_formatted_special_codes_formatting(self):
        for i in range(0, len(BAD_FORMAT_SPECIAL_CODES)):
            self.assertEqual(
                scurri_postcode.format_postcode(BAD_FORMAT_SPECIAL_CODES[i]),
                GOOD_SPECIAL_POSTCODES[i])

    def test_invalid_outward_codes_formatting(self):
        for postcode in INVALID_OUTWARD_CODES:
            self.assertRaises(
                scurri_postcode.InvalidPostcode,
                scurri_postcode.format_postcode,
                postcode)

    def test_invalid_inward_codes_formatting(self):
        for postcode in INVALID_INWARD_CODES:
            self.assertRaises(
                scurri_postcode.InvalidPostcode,
                scurri_postcode.format_postcode,
                postcode)

    def test_invalid_characters_codes_formatting(self):
        for postcode in INVALID_CHARACTER_CODES:
            self.assertRaises(
                scurri_postcode.InvalidPostcode,
                scurri_postcode.format_postcode,
                postcode)


if __name__ == '__main__':
    unittest.main()
