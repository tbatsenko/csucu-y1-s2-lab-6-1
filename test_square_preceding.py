from square_processing import square_preceding
import unittest


class TestSquareProcessing(unittest.TestCase):

    def test_is_working(self):
        self.assertEqual(square_preceding([1, 2, 3]), [0, 1, 4])

    def test_first_zero(self):
        self.assertTrue(square_preceding([0, 1, 4]))
        self.assertFalse([1, 4, 9])


if __name__ == '__main__':
    unittest.main()
