import unittest
from scurripostcode import scurri_postcode

GOOD_STANDARD_POSTCODES = ["EC1A 1BB",
                           "W1A 0AX",
                           "M1 1AE",
                           "B33 8TH",
                           "CR2 6XH",
                           "DN55 1PT",
                           "BS16 9HW"]

GOOD_SPECIAL_POSTCODES = ["AI-2640",
                           "KY1 1602",
                           "MSR 1330",
                           "VG 1140",
                           "CR 03",
                           "GE CX",
                           "BS98"]

POORLY_FORMATTED_POSTCODES = ["EC1A   1B B",
                              "  W1A 0 AX  ",
                              "M  1 1A E ",
                              "B338TH",
                              "C  R 2 6 X H",
                              "DN551     PT"]

INVALID_OUTWARD_POSTCODES = ["ECRA 1BB",
                             "WA 0AX",
                             "M 1AE",
                             "333 8TH",
                             "9R2 6XH",
                             "DN5AA 1PT"
                             "9HW"]

INVALID_INWARD_POSTCODES = ["EC1A BB",
                            "W1A ",
                            "M1 1E",
                            "B33 87H",
                            "CR2 6XNH",
                            "DN55 1PT0"
                            "BS16 9"]

INVALID_CHARACTER_POSTCODES = ["EC1A@1BB",
                               "W1A|1AX",
                               "",
                               "B33$8TH",
                               "CR2 =6XH",
                               "DN55 .1PT"]


class TestPostcodeValidation(unittest.TestCase):
    def test_uppercase_valid_codes(self):
        for postcode in GOOD_STANDARD_POSTCODES:
            self.assertTrue(scurri_postcode.validate_postcode(postcode), postcode)

    def test_lowercase_valid_codes(self):
        for postcode in GOOD_STANDARD_POSTCODES:
            self.assertTrue(scurri_postcode.validate_postcode(postcode.lower()), postcode)

    def test_poorly_formatted_valid_codes(self):
        for postcode in POORLY_FORMATTED_POSTCODES:
            self.assertTrue(scurri_postcode.validate_postcode(postcode), postcode)

    def test_special_cases_valid_codes(self):
        for postcode in GOOD_SPECIAL_POSTCODES:
            self.assertTrue(scurri_postcode.validate_postcode(postcode), postcode)

    def test_invalid_outward_codes(self):
        for postcode in INVALID_OUTWARD_POSTCODES:
            self.assertFalse(scurri_postcode.validate_postcode(postcode), postcode)

    def test_invalid_inward_codes(self):
        for postcode in INVALID_INWARD_POSTCODES:
            self.assertFalse(scurri_postcode.validate_postcode(postcode), postcode)

    def test_invalid_characters_codes(self):
        for postcode in INVALID_CHARACTER_POSTCODES:
            self.assertFalse(scurri_postcode.validate_postcode(postcode), postcode)


if __name__ == '__main__':
    unittest.main()
