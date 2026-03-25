import unittest
from example_package.example import Example

class TestExample(unittest.TestCase):
    def test_get_example_message(self):
        test_message = 'Test Message'
        example = Example(test_message)
        self.assertEqual(example.get_example_message(), test_message)

    def test_get_ascii_art(self):
        test_message = 'Test'
        example = Example(test_message)
        ascii_art = example.get_ascii_art()
        self.assertIn(' _____         _ ', ascii_art)
        self.assertIn('|_   _|__  ___| |_ ', ascii_art)
        self.assertIn('  | |/ _ \/ __| __|', ascii_art)
        self.assertIn('  | |  __/\__ \ |_', ascii_art)
        self.assertIn('  |_|\___||___/\__|', ascii_art)

if __name__ == '__main__':
    unittest.main()
