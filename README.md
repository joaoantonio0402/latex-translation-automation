# LaTeX Translation Automation

AI-powered multilingual document translation and synchronization pipeline for LaTeX projects.

## Overview

LaTeX Translation Automation is a Python-based workflow that automatically translates LaTeX documents into multiple languages using Large Language Models (LLMs).

The project was designed to simplify the maintenance of multilingual document repositories by automating:

* document translation
* file synchronization
* LaTeX generation
* PDF compilation
* Git integration

Although initially created for resumes and cover letters, the project is fully generic and can be used for any LaTeX-based documentation.

---

## Features

* Automatic translation of `.tex` files
* Multi-language synchronization
* AI-powered translation using Gemini
* Preservation of LaTeX syntax and commands
* Automatic PDF generation
* Git automation
* Template-based document generation
* Modular project structure

---

## Supported Use Cases

* Resumes
* Cover letters
* Academic papers
* Documentation
* Technical reports
* Blog posts written in LaTeX

---

## Project Structure

```text
latex-translation-automation/
│
├── content/
│   ├── pt/
│   ├── en/
│   └── template/
│
├── prompts/
│
├── scripts/
│   ├── build.py
│   ├── git_utils.py
│   └── sync.py
│
├── output/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## How It Works

1. The system detects modified files in the source language directory.
2. Modified content is sent to Gemini for translation.
3. Translated files are generated automatically.
4. LaTeX documents are compiled into PDFs.
5. Changes can optionally be committed and pushed automatically.

---

## Example Workflow

```bash
python sync.py
```

Example process:

```text
Portuguese content
        ↓
Gemini Translation
        ↓
Translated .tex files
        ↓
PDF compilation
        ↓
Git commit + push
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/latex-translation-automation.git
cd latex-translation-automation
```


## Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Requirements

* Python 3.11+
* LaTeX distribution installed

  * TeX Live
  * MiKTeX
* Gemini API key

---

## Translation Prompting

The project uses structured prompts to ensure:

* valid JSON responses
* LaTeX syntax preservation
* deterministic output formatting
* path synchronization between languages

---

## Example Input

```text
content/pt/introduction.tex
```

---

## Example Output

```text
content/en/introduction.tex
```

---

## Technologies Used

* Python
* LaTeX
* Google Gemini API
* Git
* pathlib
* subprocess

---
