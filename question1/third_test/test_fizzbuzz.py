import unittest
import fizzbuzz

class testCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(fizzbuzz.fizzBuzz(3), "Fizz")
    def test_case_2(self):
        self.assertEqual(fizzbuzz.fizzBuzz(5), "Buzz")
    def test_case_3(self):
        self.assertEqual(fizzbuzz.fizzBuzz(15), "not multiple of 3, 5, 15")
    def test_case_4(self):
        self.assertEqual(fizzbuzz.fizzBuzz(30), "FizzBuzz")
    def test_case_5(self):
        self.assertEqual(fizzbuzz.fizzBuzz(27), "Fizz")

    def test_case_6(self):
        self.assertEqual(fizzbuzz.fizzBuzz(100), "not multiple of 3, 5, 15")

    def test_case_7(self):
        self.assertEqual(fizzbuzz.fizzBuzz(40), "Buzz")
    def test_case_8(self):
        self.assertEqual(fizzbuzz.fizzBuzz(99), "FizzBuzz")
if __name__ == "__main__":
    unittest.main()