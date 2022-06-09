import unittest

import temperature_utils_v2
class TemperatureUtilsv2Test(unittest.TestCase):
    def test_kelvin_from_celsium(self):
        test_cases=[
            (32, 305.15),
            (48,321.15),
            (96,369.15),
            (15,288.15)
         ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} ->{expected}"):
                self.assertEqual(expected,temperature_utils_v2.convert_kelvin_trmp_from_celsius(temp_in))


    def test_kelvin_from_fahrenheit(self):
        test_cases = [
            (32, 273.15),
            (48, 282.04),
            (96, 308.705),
            (15, 263.70)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} ->{expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_kelvin_temp_from_fahrenheit(temp_in))

