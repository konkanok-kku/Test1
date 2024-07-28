from datetime import datetime
import unittest
from io import StringIO
import sys

class Pension:
    APPLICATION_DEADLINE = datetime(2024, 7, 31)
    RETIREMENT_AGE = 60
    COMBINED_AGE_TEACHING = 80
    MAX_BASE_SALARY = 90000
    HIGHER_BASE_PERCENTAGE = 0.016
    LOWER_BASE_PERCENTAGE = 0.0155
    EXCESS_PERCENTAGE = 0.015

    def __init__(self, application_date, birth_date, years_of_teaching, highest_salary):
        self.application_date = application_date
        self.birth_date = birth_date
        self.years_of_teaching = years_of_teaching
        self.highest_salary = highest_salary
        self.age = (application_date - birth_date).days // 365

    def is_eligible(self):
        if self.application_date > self.APPLICATION_DEADLINE:
            return False
        return self.age >= self.RETIREMENT_AGE or (self.age + self.years_of_teaching) >= self.COMBINED_AGE_TEACHING

    def calculate_pension(self):
        if not self.is_eligible():
            return None
        if self.age >= self.RETIREMENT_AGE:
            base_percentage = self.HIGHER_BASE_PERCENTAGE
        else:
            base_percentage = self.LOWER_BASE_PERCENTAGE
        if self.highest_salary <= self.MAX_BASE_SALARY:
            return self.highest_salary * base_percentage * self.years_of_teaching
        else:
            return (self.MAX_BASE_SALARY * base_percentage * self.years_of_teaching) + ((self.highest_salary - self.MAX_BASE_SALARY) * self.EXCESS_PERCENTAGE * self.years_of_teaching)

class TestPension(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def test_pension_calculation(self):
        test_cases = [
            {
                'application_date': datetime(2024, 7, 30),
                'birth_date': datetime(1964, 1, 1),
                'years_of_teaching': 30,
                'highest_salary': 80000,
                'expected_eligible': True,
                'expected_pension': 38400.0
            },
            {
                'application_date': datetime(2024, 7, 30),
                'birth_date': datetime(1964, 1, 1),
                'years_of_teaching': 30,
                'highest_salary': 100000,
                'expected_eligible': True,
                'expected_pension': 49200.0
            },
            {
                'application_date': datetime(2024, 7, 30),
                'birth_date': datetime(1969, 1, 1),
                'years_of_teaching': 25,
                'highest_salary': 80000,
                'expected_eligible': True,
                'expected_pension': 31025.0
            },
            {
                'application_date': datetime(2024, 7, 30),
                'birth_date': datetime(1969, 1, 1),
                'years_of_teaching': 25,
                'highest_salary': 100000,
                'expected_eligible': True,
                'expected_pension': 49200.0
            },
            {
                'application_date': datetime(2024, 8, 1),
                'birth_date': datetime(1964, 1, 1),
                'years_of_teaching': 30,
                'highest_salary': 80000,
                'expected_eligible': False,
                'expected_pension': None
            },
            {
                'application_date': datetime(2024, 7, 30),
                'birth_date': datetime(1969, 1, 1),
                'years_of_teaching': 25,
                'highest_salary': 100000,
                'expected_eligible': True,
                'expected_pension': 49200.0
            },
            {
                'application_date': datetime(2024, 7, 30),
                'birth_date': datetime(1974, 1, 1),
                'years_of_teaching': 20,
                'highest_salary': 80000,
                'expected_eligible': False,
                'expected_pension': None
            },
            {
                'application_date': datetime(2024, 7, 30),
                'birth_date': datetime(1974, 1, 1),
                'years_of_teaching': 20,
                'highest_salary': 100000,
                'expected_eligible': False,
                'expected_pension': None
            },
            {
                'application_date': datetime(2024, 8, 1),
                'birth_date': datetime(1974, 1, 1),
                'years_of_teaching': 20,
                'highest_salary': 100000,
                'expected_eligible': False,
                'expected_pension': None
            }
        ]

        for i, case in enumerate(test_cases, 1):
            with self.subTest(f"Rule {i}"):
                pension = Pension(case['application_date'], case['birth_date'],
                                  case['years_of_teaching'], case['highest_salary'])
                
                self.assertEqual(pension.is_eligible(), case['expected_eligible'])
                
                if case['expected_eligible']:
                    self.assertAlmostEqual(pension.calculate_pension(), case['expected_pension'], delta=0.01)
                else:
                    self.assertIsNone(pension.calculate_pension())

if __name__ == '__main__':
    unittest.main()
