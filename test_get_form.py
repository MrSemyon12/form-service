import unittest
import requests

SERVER_URL = "http://127.0.0.1:8000"
ENDPOINT_URL = "/get_form"

MATCH_CASES = [
    (
        '"customer_name=maxim&customer_email=den@mail.ru&customer_phone=+7 232 456 54 54&customer_birth_date=12.03.2001&order_date=12312313124234"',
        "CustomerForm",
    ),
    (
        '"employee_name=abacaba&employee_phone=+7 942 423 34 43&asdas=5fs2ff23"',
        "EmployeeForm",
    ),
    (
        '"employee_name=abacaba&employee_phone=+7 942 423 34 43&some_phone=adasdasd"',
        "EmployeeForm",
    ),
    (
        '"order_title=title&order_info=info&some_field=45.76.2000&order_date=23.06.2001"',
        "OrderForm",
    ),
    (
        '"feedback_info=feed&feedback_date=2020-12-11&some_field=sdsds&some_phone=+7 999 324 34 53"',
        "FeedbackForm",
    ),
]

UNMATCH_CASES = [
    (
        '"customer_name=maxim&customer_email=denmail.ru&customer_phone=+7 965 674 18 17&customer_birth_date=12.03.2001&order_date=12312313124234"',
        {
            "customer_name": "text",
            "customer_email": "text",
            "customer_phone": "phone",
            "customer_birth_date": "date",
            "order_date": "text",
        },
    ),
    (
        '"customer_date=2000-03-22&customer_email=denmail.ru&customer_phone=+7 965 674 18 17&customer_birth_date=12.03.2001&order_date=+7 8904 34 34 43"',
        {
            "customer_date": "date",
            "customer_email": "text",
            "customer_phone": "phone",
            "customer_birth_date": "date",
            "order_date": "text",
        },
    ),
    ('"customer_date=2000-03-22"', {"customer_date": "date"}),
    ('"customer_date=2000-03-2"', {"customer_date": "text"}),
    ('"customer_date=22.03.2022"', {"customer_date": "date"}),
    ('"customer_date=22.03..2022"', {"customer_date": "text"}),
    ('"customer_name=maxim"', {"customer_name": "text"}),
    ('"customer_phone=+7 423 330 00 33"', {"customer_phone": "phone"}),
    ('"customer_phone=+7 423 330 00-33"', {"customer_phone": "text"}),
    ('"customer_email=email@mail.ru"', {"customer_email": "email"}),
    ('"customer_email=emailmail.ru"', {"customer_email": "text"}),
]


class TestGetForm(unittest.TestCase):
    def test_db_match(self):
        for input, output in MATCH_CASES:
            response = requests.post(
                url=f"{SERVER_URL}{ENDPOINT_URL}", data=input
            ).json()
            self.assertEqual(response, output)

    def test_db_unmatch(self):
        for input, output in UNMATCH_CASES:
            response = requests.post(
                url=f"{SERVER_URL}{ENDPOINT_URL}", data=input
            ).json()
            self.assertEqual(response, output)


if __name__ == "__main__":
    unittest.main()
