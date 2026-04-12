"""Mock external APIs — datasets inspired by the workbook plus extra demo records."""

from __future__ import annotations

from typing import Any

DEFAULT_SCENARIO = "example_1"

# First three mirror the spreadsheet examples; the rest are additional demo vehicles.
MOCK_SCENARIOS: dict[str, dict[str, Any]] = {
    "example_1": {
        "rto": {
            "car_number": "UP 32 DY 2234",
            "car_owner": "Mr Ashok Verma",
            "registration_number": "912345678",
            "date_of_purchase": "15/01/2025",
        },
        "insurance": {
            "pan": "AU229765",
            "insurance_id": "0876IJK123",
            "service_centre": "Lucknow",
            "accidents": "No",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "No",
            "odometer": "25000",
        },
    },
    "example_2": {
        "rto": {
            "car_number": "UP 32 AU 5672",
            "car_owner": "Mrs Geeta Kumari",
            "registration_number": "412342378",
            "date_of_purchase": "02/06/2020",
        },
        "insurance": {
            "pan": "PS329776",
            "insurance_id": "7456KL745",
            "service_centre": "Lucknow",
            "accidents": "No",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "Steering wheel locks intermittently",
            "odometer": "85000",
        },
    },
    "example_3": {
        "rto": {
            "car_number": "MH 15 PQ 9745",
            "car_owner": "Mr Deepak Chopra",
            "registration_number": "812341123",
            "date_of_purchase": "06/12/2020",
        },
        "insurance": {
            "pan": "ZY562987",
            "insurance_id": "0436GR498",
            "service_centre": "Nashik",
            "accidents": "No",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "Engine overheating under load",
            "odometer": "150000",
        },
    },
    "example_4": {
        "rto": {
            "car_number": "DL 8C BF 1102",
            "car_owner": "Ms Neha Kapoor",
            "registration_number": "118823401",
            "date_of_purchase": "22/09/2022",
        },
        "insurance": {
            "pan": "CDKP9876N",
            "insurance_id": "DL-INS-88421A",
            "service_centre": "Dwarka",
            "accidents": "Yes — rear bumper replaced (2024)",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "AC compressor noisy at idle",
            "odometer": "42000",
        },
    },
    "example_5": {
        "rto": {
            "car_number": "KA 03 MJ 4410",
            "car_owner": "Mr Ravi Krishnan",
            "registration_number": "229014556",
            "date_of_purchase": "03/11/2019",
        },
        "insurance": {
            "pan": "ABRPK2290Q",
            "insurance_id": "HDFC-MV-22901",
            "service_centre": "Indiranagar",
            "accidents": "No",
        },
        "third_party": {
            "colour_change": "Yes — full respray 2021 (white to pearl white)",
            "mechanical_issues": "No",
            "odometer": "78000",
        },
    },
    "example_6": {
        "rto": {
            "car_number": "TN 09 BP 7781",
            "car_owner": "Sri Venkatesh Transport",
            "registration_number": "334009812",
            "date_of_purchase": "18/04/2018",
        },
        "insurance": {
            "pan": "AAFCV8899K",
            "insurance_id": "ICICI-COM-7712",
            "service_centre": "Guindy",
            "accidents": "Yes — left fender repaired",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "Clutch shudder in 2nd gear",
            "odometer": "198000",
        },
    },
    "example_7": {
        "rto": {
            "car_number": "RJ 14 CB 5560",
            "car_owner": "Mrs Poonam Singh",
            "registration_number": "441200998",
            "date_of_purchase": "07/02/2021",
        },
        "insurance": {
            "pan": "BXZPS1122R",
            "insurance_id": "BAJAJ-4W-33091",
            "service_centre": "Jaipur",
            "accidents": "No",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "EGR valve replaced; occasional limp mode",
            "odometer": "112500",
        },
    },
    "example_8": {
        "rto": {
            "car_number": "WB 06 AB 2214",
            "car_owner": "Mr Arindam Bose",
            "registration_number": "550901223",
            "date_of_purchase": "29/12/2020",
        },
        "insurance": {
            "pan": "ABCPB9012L",
            "insurance_id": "TATA-AIG-90881",
            "service_centre": "Salt Lake",
            "accidents": "No",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "Prior flood repair documented — electronics harness replaced",
            "odometer": "61000",
        },
    },
    "example_9": {
        "rto": {
            "car_number": "GJ 01 RT 9900",
            "car_owner": "Patel Auto Leasing Pvt Ltd",
            "registration_number": "667788990",
            "date_of_purchase": "14/08/2023",
        },
        "insurance": {
            "pan": "AAHCP4455M",
            "insurance_id": "KOTAK-MOT-12009",
            "service_centre": "Ahmedabad",
            "accidents": "No",
        },
        "third_party": {
            "colour_change": "No",
            "mechanical_issues": "No",
            "odometer": "18500",
        },
    },
    "example_10": {
        "rto": {
            "car_number": "HR 26 CJ 8844",
            "car_owner": "Mr Karan Malhotra",
            "registration_number": "998877665",
            "date_of_purchase": "01/05/2017",
        },
        "insurance": {
            "pan": "DEFPM8899N",
            "insurance_id": "RELI-VEH-44002",
            "service_centre": "Gurgaon",
            "accidents": "Yes — windscreen & roof rail replaced (hail)",
        },
        "third_party": {
            "colour_change": "Yes — roof and bonnet resprayed",
            "mechanical_issues": "Rear suspension bush wear",
            "odometer": "134200",
        },
    },
}

SCENARIO_CHOICES: list[tuple[str, str]] = [
    ("example_1", "Example 1 — Lucknow / UP 32 DY 2234"),
    ("example_2", "Example 2 — UP 32 AU 5672"),
    ("example_3", "Example 3 — MH 15 PQ 9745 (Nashik)"),
    ("example_4", "Example 4 — Delhi / DL 8C BF 1102 (minor claim)"),
    ("example_5", "Example 5 — Bengaluru / KA 03 MJ 4410 (respray)"),
    ("example_6", "Example 6 — Chennai / TN 09 BP 7781 (high km)"),
    ("example_7", "Example 7 — Jaipur / RJ 14 CB 5560 (diesel EGR)"),
    ("example_8", "Example 8 — Kolkata / WB 06 AB 2214 (flood repair)"),
    ("example_9", "Example 9 — Ahmedabad / GJ 01 RT 9900 (nearly new)"),
    ("example_10", "Example 10 — Gurgaon / HR 26 CJ 8844 (hail + suspension)"),
]


def call_rto_api(scenario: str) -> dict[str, Any]:
    data = MOCK_SCENARIOS.get(scenario, MOCK_SCENARIOS[DEFAULT_SCENARIO])[
        "rto"
    ].copy()
    return {"provider": "RTO (mock)", "status": "ok", "data": data}


def call_insurance_api(scenario: str) -> dict[str, Any]:
    data = MOCK_SCENARIOS.get(scenario, MOCK_SCENARIOS[DEFAULT_SCENARIO])[
        "insurance"
    ].copy()
    return {"provider": "Insurance company (mock)", "status": "ok", "data": data}


def call_third_party_api(scenario: str) -> dict[str, Any]:
    data = MOCK_SCENARIOS.get(scenario, MOCK_SCENARIOS[DEFAULT_SCENARIO])[
        "third_party"
    ].copy()
    return {
        "provider": "Automobile verification service (mock)",
        "status": "ok",
        "data": data,
    }
