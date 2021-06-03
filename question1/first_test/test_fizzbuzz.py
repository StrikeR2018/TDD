import unittest
import fizzbuzz

class testCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(fizzbuzz.fizzBuzz(3), "Fizz")
    def test_case_2(self):
        self.assertEqual(fizzbuzz.fizzBuzz(5), "Buzz")
    def test_case_3(self):
        self.assertEqual(fizzbuzz.fizzBuzz(15), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()