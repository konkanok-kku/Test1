class Commission:
    PRICE_STOCK = 4500.0
    PRICE_LOCK = 3000.0
    PRICE_BARREL = 2500.0

    def check_commission(self, num_lock: int, num_stock: int, num_barrel: int) -> float:
        """
        Calculates the commission based on the number of locks, stocks, and barrels sold.

        Args:
            num_lock: The number of locks sold.
            num_stock: The number of stocks sold.
            num_barrel: The number of barrels sold.

        Returns:
            The calculated commission, or -1.0 if any input is negative.
        """

        if num_lock < 0 or num_stock < 0 or num_barrel < 0:
            return -1.0

        sold_lock = num_lock * self.PRICE_LOCK
        sold_stock = num_stock * self.PRICE_STOCK
        sold_barrel = num_barrel * self.PRICE_BARREL

        total_sales = sold_lock + sold_stock + sold_barrel

        if total_sales > 50000:
            commission = (0.1 * 20000) + (0.15 * 30000)
            commission += 0.2 * (total_sales - 50000)
        elif 20000 < total_sales < 50000:
            commission = 0.1 * 20000
            commission += 0.15 * (total_sales - 20000)
        elif 10000 < total_sales < 20000:
            commission = 0.1 * total_sales
        else:
            commission = 0.0

        return commission


import unittest
import time

class TestCommission(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up the test suite...")
        cls.test_data = [
            (1, 1, 1, 1000.0),
            (10, 10, 10, 10000.0),
            (20, 20, 20, 24000.0),
            (30, 30, 30, 40500.0),
        ]

    @classmethod
    def tearDownClass(cls):
        print("Cleaning up after all tests...")
        cls.test_data = None

    def setUp(self):
        print("Setting up a test...")
        self.commission = Commission()
        self.start_time = time.time()

    def tearDown(self):
        print("Cleaning up after a test...")
        self.commission = None
        end_time = time.time()
        print(f"Test duration: {end_time - self.start_time:.6f} seconds")

    def test_normal_cases(self):
        for num_lock, num_stock, num_barrel, expected in self.test_data:
            with self.subTest(num_lock=num_lock, num_stock=num_stock, num_barrel=num_barrel):
                result = self.commission.check_commission(num_lock, num_stock, num_barrel)
                self.assertAlmostEqual(result, expected, places=2)

    def test_boundary_cases(self):
        test_cases = [
            (0, 0, 0, 0.0),
            (6, 2, 2, 5700.0),  #at 30000
            (13, 5, 4, 16700.0),  #at 50000
        ]
        for num_lock, num_stock, num_barrel, expected in test_cases:
            with self.subTest(num_lock=num_lock, num_stock=num_stock, num_barrel=num_barrel):
                result = self.commission.check_commission(num_lock, num_stock, num_barrel)
                self.assertAlmostEqual(result, expected, places=2)

    def test_special_cases(self):
        result = self.commission.check_commission(100, 100, 100)
        self.assertAlmostEqual(result, 200000.0, places=2)

    def test_negative_input_cases(self):
        test_cases = [
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1),
            (-1, -1, -1),
        ]
        for num_lock, num_stock, num_barrel in test_cases:
            with self.subTest(num_lock=num_lock, num_stock=num_stock, num_barrel=num_barrel):
                result = self.commission.check_commission(num_lock, num_stock, num_barrel)
                self.assertEqual(result, -1.0)

    def test_mixed_cases(self):
        test_cases = [
            (5, 3, 0, 4725.0),
            (0, 10, 5, 6375.0),
        ]
        for num_lock, num_stock, num_barrel, expected in test_cases:
            with self.subTest(num_lock=num_lock, num_stock=num_stock, num_barrel=num_barrel):
                result = self.commission.check_commission(num_lock, num_stock, num_barrel)
                self.assertAlmostEqual(result, expected, places=2)

    def test_edge_cases(self):
        # Very large numbers
        result = self.commission.check_commission(50000, 50000, 50000)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)

        result = self.commission.check_commission(int(0.5), int(0.5), int(0.5))
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            self.commission.check_commission("1", 1, 1)
        with self.assertRaises(TypeError):
            self.commission.check_commission(1, "1", 1)
        with self.assertRaises(TypeError):
            self.commission.check_commission(1, 1, "1")

    def test_zero_commission_case(self):
        result = self.commission.check_commission(1, 1, 1)
        self.assertGreater(result, 0)

    def test_consistency(self):
        for _ in range(100):
            result1 = self.commission.check_commission(10, 10, 10)
            result2 = self.commission.check_commission(10, 10, 10)
            self.assertEqual(result1, result2, "Results should be consistent for the same input")


    def test_floating_point_precision(self):
        result = self.commission.check_commission(33, 33, 33)
        expected = 44550.0
        self.assertAlmostEqual(result, expected, places=10, msg="Floating point precision should be high")

if __name__ == '__main__':
    unittest.main()
