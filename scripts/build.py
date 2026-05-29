from pathlib import Path
import subprocess

# =========================================================
# BASE PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CONTENT_DIR = BASE_DIR / "content"
TEMPLATE_DIR = CONTENT_DIR / "template"
OUTPUT_DIR = BASE_DIR / "output"


# =========================================================
# TEMPLATE FILES
# =========================================================

ORDER_FILE = TEMPLATE_DIR / "sections_order.txt"
PREAMBLE_FILE = TEMPLATE_DIR / "preamble.tex"


def load_order(order_path: Path) -> list[str]:

    return [
        line.strip()
        for line in order_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

def build_language(language: str, order: list[str]) -> dict[str, str]:

    content = {}

    for section in order:

        file_path = CONTENT_DIR / language / f"{section}.tex"

        if file_path.exists():
            content[section] = file_path.read_text(encoding="utf-8")

    return content

def render_tex(content: dict[str, str]) -> str:

    template = (TEMPLATE_DIR / "template.tex").read_text(encoding="utf-8")
    preamble = (PREAMBLE_FILE).read_text(encoding="utf-8")

    full_content = "\n\n".join(content.values())

    return template.replace("{{PREAMBLE}}", preamble).replace("{{CONTENT}}", full_content)

def save_output(language: str, tex: str):

    output_dir = OUTPUT_DIR / language
    output_dir.mkdir(parents=True, exist_ok=True)

    tex_path = output_dir / f"CV_João_Gonçalves_2026.tex"

    tex_path.write_text(tex, encoding="utf-8")

    return tex_path

def compile_pdf(tex_path: Path):

    subprocess.run([
        "pdflatex",
        "-output-directory",
        str(tex_path.parent),
        str(tex_path.name)
    ], cwd=BASE_DIR, check=True)

def build(language: str):

    order = load_order(ORDER_FILE)

    content = build_language(language, order)

    tex = render_tex(content)

    tex_path = save_output(language, tex)

    compile_pdf(tex_path)
