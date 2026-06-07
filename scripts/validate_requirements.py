import re

with open("requirements/requirements.md") as file:
    text = file.read()

requirements = re.findall(r"REQ-\d+", text)

print("Requirements Found:")

for req in requirements:
    print(req)

print()
print("Total Requirements:", len(requirements))
