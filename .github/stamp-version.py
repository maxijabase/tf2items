"""Write the git tag into the extension version header before compile."""
import os
import re
from pathlib import Path

ref = os.environ["GITHUB_REF_NAME"]
version = ref[1:] if ref.startswith("v") else ref
match = re.match(r"(\d+)\.(\d+)\.(\d+)", version)
if not match:
    raise SystemExit(f"tag {ref} does not start with a numeric version")
major, minor, patch = match.groups()

header = Path("extension/version.h")
text = header.read_text(encoding="utf-8")
replacements = {
    "SM_BUILD_TAG": '""',
    "SM_BUILD_UNIQUEID": f'"{ref}"',
    "SM_VERSION": f'"{major}.{minor}.{patch}"',
    "SM_FILE_VERSION": f"{major},{minor},{patch},0",
}
for name, value in replacements.items():
    text, count = re.subn(
        rf"(#define\s+{name}\s+)[^\r\n]+",
        rf"\g<1>{value}",
        text,
        count=1,
    )
    if count != 1:
        raise SystemExit(f"did not find #define {name} in {header}")
header.write_text(text, encoding="utf-8")
print(f"stamped {ref} -> {major}.{minor}.{patch}")
