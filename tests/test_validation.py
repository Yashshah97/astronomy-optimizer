import unittest
from astronomy_optimizer import validation

class TestValidation(unittest.TestCase):

    def test_validate_positive_integer(self):
        self.assertEqual(validation._validate_positive_integer(1, "x"), None)
        with self.assertRaises(validation.InvalidInput):
            validation._validate_positive_integer(-1, "x")
        with self.assertRaises(validation.InvalidInput):
            validation._validate_positive_integer(0, "x")
        with self.assertRaises(validation.InvalidInput):
            validation._validate_positive_integer("a", "x")

    def test_validate_non_negative_integer(self):
        self.assertEqual(validation._validate_non_negative_integer(1, "x"), None)
        self.assertEqual(validation._validate_non_negative_integer(0, "x"), None)
        with self.assertRaises(validation.InvalidInput):
            validation._validate_non_negative_integer(-1, "x")
        with self.assertRaises(validation.InvalidInput):
            validation._validate_non_negative_integer("a", "x")

    def test_validate_float(self):
        self.assertEqual(validation._validate_float(1.0, "x"), None)
        with self.assertRaises(validation.InvalidInput):
            validation._validate_float(-1.0, "x")
        with self.assertRaises(validation.InvalidInput):
            validation._validate_float("a", "x")

    def test_validate_string(self):
        self.assertEqual(validation._validate_string("a", "x"), None)
        with self.assertRaises(validation.InvalidInput):
            validation._validate_string(1, "x")


if __name__ == "__main__":
    unittest.main()
