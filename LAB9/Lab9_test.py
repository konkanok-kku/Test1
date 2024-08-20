#Kornkanok Pruttipan
#653380187-0 Sec.2
#Lab9


import requests
from datetime import datetime
from unittest.mock import Mock, patch
import unittest

class CurrencyExchanger:
    def __init__(self, base_currency="THB", target_currency="USD"):
        self.currency_api = "https://coc-kku-bank.com/foreign-exchange"
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.ex_date = datetime.today().date()
        self.api_response = None

    def get_currency_rate(self):
        try:
            p = {'from': self.base_currency, 'to': self.target_currency}
            response = requests.get(self.currency_api, params=p)
            if response.status_code in (200, 201):
                self.api_response = response.json()
        except requests.exceptions.RequestException:
            self.api_response = None

    def currency_exchange(self, amount):
        self.get_currency_rate()
        if self.api_response and 'rate' in self.api_response:
            rate = self.api_response['rate']
            return amount * rate
        return None

class TestCurrencyExchanger(unittest.TestCase):
    @patch('requests.get')
    def test_currency_exchange(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'rate': 30.5}
        mock_get.return_value = mock_response

        exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")
        result = exchanger.currency_exchange(1000)
        self.assertEqual(result, 30500)

        print(f"ทดสอบการแปลง 1000 THB เป็น KRW")
        print(f"ผลลัพธ์: {result} KRW")
        print(f"คาดหวัง: 30500 KRW")
        print(f"ผลการทดสอบ: {'ผ่าน' if result == 30500 else 'ไม่ผ่าน'}")

if __name__ == '__main__':

    unittest.main(exit=False)


    print("\nทดสอบการแปลงสกุลเงิน")
    base_amount = float(input("ป้อนจำนวนเงินบาท: "))
    
    exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")
    
    # จำลองการตอบกลับของ API
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'rate': 30.5}
        mock_get.return_value = mock_response
        
        result = exchanger.currency_exchange(base_amount)
    
    print(f"{base_amount} THB = {result} KRW")
