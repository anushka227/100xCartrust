"""Field definitions aligned with Car Trust Data set (1).xlsx layout."""

from dataclasses import dataclass
from typing import Literal

Source = Literal["rto", "insurance", "third_party"]


@dataclass(frozen=True)
class FieldSpec:
    key: str
    label: str
    source: Source
    input_type: str  # text, date, number, textarea
    placeholder: str = ""


# Row 2 in sheet; column E is example/helper text in the workbook — we use one date field (D).
FIELDS: list[FieldSpec] = [
    FieldSpec("car_number", "Car Number", "rto", "text", "e.g. UP 32 DY 2234"),
    FieldSpec("car_owner", "Car owner", "rto", "text", "Registered owner name"),
    FieldSpec(
        "registration_number",
        "Regestration Number",
        "rto",
        "text",
        "As on RC",
    ),
    FieldSpec("date_of_purchase", "Date of Purchase", "rto", "date", "dd/mm/yyyy"),
    FieldSpec(
        "pan",
        "PAN details of owner",
        "insurance",
        "text",
        "Linked to loan / KYC",
    ),
    FieldSpec("insurance_id", "Car Insurance ID", "insurance", "text"),
    FieldSpec("service_centre", "Service Centre", "insurance", "text"),
    FieldSpec("accidents", "Accidents", "insurance", "text", "Yes / No"),
    FieldSpec("colour_change", "Colour change", "third_party", "text", "Yes / No"),
    FieldSpec(
        "mechanical_issues",
        "Any mechanical issues in car",
        "third_party",
        "textarea",
    ),
    FieldSpec("odometer", "Odometer reading", "third_party", "number", "km"),
]

SOURCE_LABELS = {
    "rto": "RTO",
    "insurance": "Insurance company",
    "third_party": "Third party verification",
}
