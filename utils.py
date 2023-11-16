from datetime import datetime
import re
from db import FieldType

DATE_REGEX = re.compile(r"^(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$")
PHONE_REGEX = re.compile(r"^\+7 \d{3} \d{3} \d{2} \d{2}$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def parse_form_data(form_data: str) -> list:
    return [tuple(pair.split("=")) for pair in form_data.split("&")]


def get_marked_form(fields: list) -> dict:
    return {k: mark_field(v) for k, v in fields}


def mark_field(field: str) -> str:
    if bool(DATE_REGEX.match(field)):
        formats = ["%d.%m.%Y", "%Y-%m-%d"]

        for date_format in formats:
            try:
                datetime.strptime(field, date_format)
                return FieldType.DATE.value
            except ValueError:
                continue

        return FieldType.TEXT.value

    if bool(PHONE_REGEX.match(field)):
        return FieldType.PHONE.value

    if bool(EMAIL_REGEX.match(field)):
        return FieldType.EMAIL.value

    return FieldType.TEXT.value


def find_matching_template(templates: list[dict], form: dict) -> str | None:
    for template in templates:
        if all(
            form.get(field_name) == field_type
            for field_name, field_type in template.items()
            if field_name != "name"
        ):
            return template["name"]
    return None
