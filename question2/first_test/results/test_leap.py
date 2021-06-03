import unittest
import leap_year

class testCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(leap_year.leap_year(2000), "This is a leap year.")
    def test_case_2(self):
            self.assertEqual(leap_year.leap_year(2001), "This is not a leap year.")
    def test_case_3(self):
            self.assertEqual(leap_year.leap_year(2021), "This is not a leap year.")
    def test_case_4(self):
            self.assertEqual(leap_year.leap_year(2020), "This is a leap year.")
    def test_case_5(self):
            self.assertEqual(leap_year.leap_year(2033), "This is not a leap year.")
    def test_case_6(self):
            self.assertEqual(leap_year.leap_year(2032), "This is a leap year.")
if __name__ == "__main__":
    unittest.main()