import unittest
from astronomy_optimizer import analysis

class TestAnalysis(unittest.TestCase):

    def test_calculate_distance(self):
        ra1, dec1 = 0.5, 0.3
        ra2, dec2 = 0.7, 0.4
        distance = analysis.calculate_distance(ra1, dec1, ra2, dec2)
        self.assertGreater(distance, 0)

    def test_calculate_magnitude(self):
        mag = 10.5
        distance = 100
        magnitude = analysis.calculate_magnitude(mag, distance)
        self.assertIsInstance(magnitude, float)

    def test_calculate_uncertainty(self):
        values = [1, 2, 3, 4, 5]
        mean, std_dev = analysis.calculate_uncertainty(values)
        self.assertGreater(mean, 0)
        self.assertGreater(std_dev, 0)

if __name__ == '__main__':
    unittest.main()
