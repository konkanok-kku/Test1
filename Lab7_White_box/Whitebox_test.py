#Konkanok Pruttipan
#653380187-0 Sec.2
#Lab7_White_box_test


import unittest

class CountClump:
    @staticmethod
    def count_clumps(nums):
        if nums is None or len(nums) == 0:  # Branch 1
            return 0
        count = 0
        prev = nums[0]
        in_clump = False
        for i in range(1, len(nums)):
            if nums[i] == prev and not in_clump:  # Branch 2
                in_clump = True
                count += 1
            elif nums[i] != prev:  # Branch 3
                prev = nums[i]
                in_clump = False
        return count

class TestCountClump(unittest.TestCase):

    def setUp(self):
        self.test_cases = {
            "test_case_1": (None, 0),
            "test_case_2": ([], 0),
            "test_case_3": ([1, 2, 3, 4], 0),
            "test_case_4": ([1, 1, 2, 2, 3, 3], 3),
            "test_case_5": ([1, 1, 2, 2, 3, 3, 4, 4, 4, 1], 4),
        }

    def tearDown(self):
        pass

    def test_count_clumps(self):
        for key, (nums, expected) in self.test_cases.items():
            with self.subTest(key=key):
                result = CountClump.count_clumps(nums)
                self.assertEqual(result, expected, f"Failed for {key}")

if __name__ == '__main__':
    unittest.main()
