import unittest
from astronomy_optimizer import models

class TestModels(unittest.TestCase):

    def test_star(self):
        star = models.Star("Alpha Centauri", 14.23, -62.67, 0.1)
        self.assertEqual(star.name, "Alpha Centauri")
        self.assertAlmostEqual(star.ra, 14.23)
        self.assertAlmostEqual(star.dec, -62.67)
        self.assertAlmostEqual(star.magnitude, 0.1)

    def test_light_curve(self):
        light_curve = models.LightCurve("Alpha Centauri", [1.0, 2.0, 3.0], [10.0, 20.0, 30.0])
        self.assertEqual(light_curve.star_name, "Alpha Centauri")
        self.assertEqual(len(light_curve.time_points), 3)
        self.assertEqual(len(light_curve.flux_values), 3)

    def test_parameter_set(self):
        star1 = models.Star("Alpha Centauri", 14.23, -62.67, 0.1)
        star2 = models.Star("Betelgeuse", 5.42, 7.19, 0.2)
        light_curve1 = models.LightCurve("Alpha Centauri", [1.0, 2.0, 3.0], [10.0, 20.0, 30.0])
        parameter_set = models.ParameterSet([star1, star2], [light_curve1])
        self.assertEqual(len(parameter_set.stars), 2)
        self.assertEqual(len(parameter_set.light_curves), 1)

if __name__ == "__main__":
    unittest.main()
