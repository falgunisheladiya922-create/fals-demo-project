import re

with open("requirements/requirements.md") as file:
    req_text = file.read()

requirements = set(
    re.findall(r"REQ-\d+", req_text)
)

with open("traceability/traceability.md") as file:
    trace_text = file.read()

trace_reqs = set(
    re.findall(r"REQ-\d+", trace_text)
)

missing = requirements - trace_reqs

if missing:
    print("Missing traceability:")
    for req in missing:
        print(req)
else:
    print("All requirements traceable")
