import unittest

from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    stub = Calculator()

    def test_empty(self):
        self.assertEqual(self.stub.add(""), 0)

    def test_single(self):
        self.assertEqual(self.stub.add("1"), 1)

    def test_two(self):
        self.assertEqual(self.stub.add("1,2"), 3)

    def test_two(self):
        self.assertEqual(self.stub.add("1,2,1"), 4)

    def test_newline_delim(self):
        self.assertEqual(self.stub.add("1\n2,3"), 6)

    def test_given_delim(self):
        self.assertEqual(self.stub.add("//;\n1;2"), 3)

    def test_negative(self):
        with self.assertRaises(Exception) as context:
            self.stub.add("-1")
            print str(context.exception)
        self.assertTrue('negatives not allowed [-1]' in str(context.exception))

    def test_limit(self):
        self.assertEqual(self.stub.add("1001,2"), 2)

    def test_delim_in_bracket(self):
        self.assertEqual(self.stub.add("//[***]\n1***2***3"), 6)

    def test_multiple_delim_in_bracket(self):
        self.assertEqual(self.stub.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_longdelim_in_bracket(self):
        self.assertEqual(self.stub.add("//[***][%%%]\n1***2%%%3"), 6)

if __name__ == '__main__':
    unittest.main()
