import unittest
from scurripostcode import scurri_postcode

class TestPostcodeValidation(unittest.TestCase):
    def test_valid_code(self):
        self.assertEqual(scurri_postcode.validate_postcode("EC1A 1BB"), True)


if __name__ == '__main__':
    unittest.main()
