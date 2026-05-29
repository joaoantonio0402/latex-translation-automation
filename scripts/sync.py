from pathlib import Path

from build import build
from gemini.translator import gemini_translate

import git_utils


# =========================================================
# DIRECTORIES
# =========================================================

PT_DIR = Path("content/pt")

# =========================================================
# GET MODIFIED FILES FROM GIT
# =========================================================

git_result = git_utils.git_compare_versions()

modified_files = []

for line in git_result.stdout.splitlines():

    status = line[:2].strip()
    file_path = line[3:]

    if status in {"M", "A", "??"}:
        modified_files.append(Path(file_path))


# =========================================================
# FILTER ONLY PORTUGUESE CONTENT FILES
# =========================================================

modified_pt_files = [
    file
    for file in modified_files
    if str(file).startswith(str(PT_DIR))
]


# =========================================================
# READ FILE CONTENTS
# =========================================================

pt_file_contents = {}

for file in modified_pt_files:

    content = file.read_text(encoding="utf-8")

    pt_file_contents[str(file)] = content

print(pt_file_contents)
# =========================================================
# TRANSLATE CONTENTS TO ENGLISH
# =========================================================

translated_contents = {}

target_languages = ["en", "es", "de"]

if pt_file_contents:
    translated_contents = gemini_translate(
        pt_file_contents,
        target_languages=target_languages
    )




# =========================================================
# WRITE TRANSLATED FILES
# =========================================================

for file_path, translated_content in translated_contents.items():

    path = Path(file_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        translated_content,
        encoding="utf-8"
    )


# =========================================================
# BUILD PDF FILES
# =========================================================

build(language="pt")
build(language="en")
build(language="es")
build(language="de")


# =========================================================
# CREATE COMMIT MESSAGE
# =========================================================

changed_files = [
    file.name
    for file in modified_pt_files
]

commit_message = (
    "auto update: "
    + ", ".join(changed_files)
)


# =========================================================
# COMMIT AND PUSH
# =========================================================

git_response = git_utils.git_commit(commit_message)

print(git_response["commit"].stdout)
print(git_response["push"].stdout)