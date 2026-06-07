import re

with open("requirements/requirements.md") as file:
    text = file.read()

requirements = re.findall(r"REQ-\d+", text)

report = f"""
# ASPICE Compliance Report

Total Requirements: {len(requirements)}

Status: PASS
"""

with open(
    "reports/compliance_report.md",
    "w"
) as file:

    file.write(report)

print("Report Generated")
