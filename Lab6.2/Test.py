import unittest
from datetime import datetime

class Pension:
    """
    แทนตัวคำนวณบำนาญสำหรับครูตามเกณฑ์ที่กำหนด
    """

    # ค่าคงที่ของคลาสสำหรับการคำนวณบำนาญ
    APPLICATION_DEADLINE = datetime(2024, 7, 31)
    RETIREMENT_AGE = 60
    COMBINED_AGE_TEACHING = 80
    MAX_BASE_SALARY = 90000
    HIGHER_BASE_PERCENTAGE = 0.016
    LOWER_BASE_PERCENTAGE = 0.0155
    EXCESS_PERCENTAGE = 0.015

    def __init__(self, application_date, birth_date, years_of_teaching, highest_salary):
        """
        สร้างออบเจ็กต์ Pension ด้วยข้อมูลของครู

        อาร์กิวเมนต์:
            application_date: ออบเจ็กต์ Datetime ที่แสดงวันที่สมัคร
            birth_date: ออบเจ็กต์ Datetime ที่แสดงวันเกิดของครู
            years_of_teaching: จำนวนเต็มที่แสดงจำนวนปีที่สอน
            highest_salary: จำนวนทศนิยมที่แสดงเงินเดือนสูงสุดของครู
        """
        self.application_date = application_date
        self.birth_date = birth_date
        self.years_of_teaching = years_of_teaching
        self.highest_salary = highest_salary
        self.age = (application_date - birth_date).days // 365

    def is_eligible(self):
        """
        ตรวจสอบว่าครูมีสิทธิ์ได้รับบำนาญหรือไม่

        คืนค่า:
            True ถ้ามีสิทธิ์, False ถ้าไม่มีสิทธิ์
        """
        if self.application_date > self.APPLICATION_DEADLINE:
            print("พลาดกำหนดส่งคำร้อง.")
            return False
        return self.age >= self.RETIREMENT_AGE or (self.age + self.years_of_teaching) >= self.COMBINED_AGE_TEACHING

    def calculate_pension(self):
        """
        คำนวณจำนวนบำนาญถ้าครูมีสิทธิ์

        คืนค่า:
            จำนวนบำนาญที่คำนวณได้เป็นทศนิยม, หรือ None ถ้าไม่มีสิทธิ์
        """
        if self.is_eligible():
            if self.age >= self.COMBINED_AGE_TEACHING:
                base_percentage = self.LOWER_BASE_PERCENTAGE
            elif self.age >= self.RETIREMENT_AGE:
                base_percentage = self.HIGHER_BASE_PERCENTAGE
            else:
                base_percentage = self.years_of_teaching / 100

            if self.highest_salary <= self.MAX_BASE_SALARY:
                return self.highest_salary * base_percentage * self.years_of_teaching
            else:
                base_pension = self.MAX_BASE_SALARY * base_percentage * self.years_of_teaching
                excess_pension = (self.highest_salary - self.MAX_BASE_SALARY) * self.EXCESS_PERCENTAGE * self.years_of_teaching
                return base_pension + excess_pension
        else:
            print("ยังไม่มีสิทธิ์ได้รับบำนาญ.")
            return None


class TestPension(unittest.TestCase):
    
    def setUp(self):
        """
        เรียกใช้ก่อนการทดสอบแต่ละครั้ง
        """
        self.test_cases = [
            (datetime(2024, 7, 30), datetime(1963, 5, 10), 30, 85000, 40800),
            (datetime(2024, 7, 30), datetime(1963, 5, 10), 30, 110000, 52200),
            (datetime(2024, 7, 30), datetime(1964, 1, 1), 15, 85000, 20400),
            (datetime(2024, 7, 30), datetime(1964, 1, 1), 15, 100000, 23175),
            (datetime(2024, 7, 30), datetime(1970, 1, 1), 26, 85000, 34255),
            (datetime(2024, 7, 30), datetime(1970, 1, 1), 26, 100000, 39780),
            (datetime(2024, 7, 30), datetime(1980, 1, 1), 15, 60000, None),
            (datetime(2024, 7, 30), datetime(1963, 5, 10), 30, 100000, None)
        ]
    
    def tearDown(self):
        """
        เรียกใช้หลังการทดสอบแต่ละครั้ง
        """
        self.test_cases = None

    def test_calculate_pension(self):
        for i, (app_date, birth_date, years_teaching, salary, expected) in enumerate(self.test_cases):
            with self.subTest(i=i):
                pension = Pension(app_date, birth_date, years_teaching, salary)
                result = pension.calculate_pension()
                self.assertEqual(result, expected, f"กรณีทดสอบ {i+1} ล้มเหลว: คาดหวัง {expected}, ได้ผลลัพธ์ {result}")

if __name__ == '__main__':
    unittest.main()
