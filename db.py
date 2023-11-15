from enum import Enum
from tinydb import TinyDB


class FieldType(Enum):
    EMAIL = "email"
    PHONE = "phone"
    DATE = "date"
    TEXT = "text"


db = TinyDB("db.json")

TEMPLATES = [
    {
        "name": "CustomerForm",
        "customer_name": FieldType.TEXT.value,
        "customer_email": FieldType.EMAIL.value,
        "customer_phone": FieldType.PHONE.value,
        "customer_birth_date": FieldType.DATE.value,
    },
    {
        "name": "EmployeeForm",
        "employee_name": FieldType.TEXT.value,
        "employee_phone": FieldType.PHONE.value,
    },
    {
        "name": "OrderForm",
        "order_title": FieldType.TEXT.value,
        "order_info": FieldType.TEXT.value,
        "order_date": FieldType.DATE.value,
    },
    {
        "name": "FeedbackForm",
        "feedback_info": FieldType.TEXT.value,
        "feedback_date": FieldType.DATE.value,
    },
]

# db.insert_multiple(TEMPLATES)
