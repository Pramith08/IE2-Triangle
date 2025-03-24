import unittest
from isTriangle import Triangle

SCALENE = Triangle.Type.SCALENE
EQUILATERAL = Triangle.Type.EQUILATERAL
ISOSCELES = Triangle.Type.ISOSCELES
INVALID = Triangle.Type.INVALID

test_cases_arr = {
    "valid": [
        {"sides": (3, 4, 5), "expected": SCALENE},
        {"sides": (51, 51, 51), "expected": EQUILATERAL},
        {"sides": (2, 2, 3), "expected": ISOSCELES},
        {"sides": (7, 10, 5), "expected": SCALENE},
        {"sides": (6, 6, 10), "expected": ISOSCELES},
        {"sides": (5, 12, 13), "expected": SCALENE},
        {"sides": (89, 89, 89), "expected": EQUILATERAL}
    ],
    "invalid": [
        {"sides": (1, 2, 3), "expected": INVALID},
        {"sides": (5, 1, 1), "expected": INVALID},
        {"sides": (0, 4, 5), "expected": INVALID},
        {"sides": (-1, 4, 5), "expected": INVALID},
        {"sides": (10, 2, 2), "expected": INVALID},
        {"sides": (1, 1, 2), "expected": INVALID}
    ],
    "edge": [
        {"sides": (0, 0, 0), "expected": INVALID},
        {"sides": (100, 1, 1), "expected": INVALID},
        {"sides": (2, 2, 4), "expected": INVALID},
        {"sides": (2, 3, 2), "expected": ISOSCELES},
        {"sides": (3, 3, 5), "expected": ISOSCELES}
    ],
}

class TriangleTestCases(unittest.TestCase):
    def check_traingular_classification(self, a, b, c, expected_type):
        self.assertEqual(Triangle.classify(a, b, c), expected_type)

    def process_test_cases(self, test_group):
        for scenario in test_group:
            self.check_traingular_classification(*scenario["sides"], scenario["expected"])

    def test_for_valid_case(self):
        self.process_test_cases(test_cases_arr["valid"])

    def test_for_invalid_case(self):
        self.process_test_cases(test_cases_arr["invalid"])

    def test_for_boundary_case(self):
        self.process_test_cases(test_cases_arr["edge"])

if __name__ == '__main__':
   unittest.main()