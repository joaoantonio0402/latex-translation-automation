from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

BASE_DIR = Path(__file__).resolve().parent.parent


CHANGE_HISTORY_FILE = Path("change_history.txt")

# def log_changes(files: list[str], target_language: str):

#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     log = (
#         f"[{timestamp}]\n"
#         f"TARGET LANGUAGE: {target_language}\n\n"
#         f"UPDATED FILES:\n"
#     )

#     for file in files:
#         log += f"- {file}\n"

#     log += "\n" + "-" * 60 + "\n\n"

#     with open(CHANGE_HISTORY_FILE, "a", encoding="utf-8") as f:
#         f.write(log)


def gemini_translate(files: dict[str, str], target_languages: list[str]) -> dict[str, str]:
    
    PROMPT_FILE = BASE_DIR / "prompts" / f"prompt.txt"

    prompt = PROMPT_FILE.read_text(encoding="utf-8")

    prompt = prompt.format(
        target_languages=", ".join(target_languages),
    )

    # transforma o dicionário em JSON formatado
    files_json = json.dumps(files, ensure_ascii=False, indent=2)

    full_prompt = (
        prompt
        + "\n\n"
        + files_json
    )
    
    print("\n" + "=" * 80)
    print("PROMPT ENVIADO PARA O GEMINI")
    print("=" * 80)
    print(full_prompt)
    print("=" * 80 + "\n")

    response = model.generate_content(full_prompt)

    print("\n" + "=" * 80)
    print("RESPOSTA DO GEMINI")
    print("=" * 80)
    print(response.text)
    print("=" * 80 + "\n")

    # converte resposta da IA em dict
    translated_files = json.loads(response.text)

    return translated_files
