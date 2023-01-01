import unittest
from client import getRatio


class MyTestCase(unittest.TestCase):
    def test_getRatio(self):
        self.assertAlmostEqual(getRatio(182, 180), 1.0111111111)
        self.assertAlmostEqual(getRatio(180, 0), 180)
        self.assertEqual(getRatio(100, 0), 100)
        


if __name__ == '__main__':
    unittest.main()
