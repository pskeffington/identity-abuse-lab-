from pathlib import Path

SECTION_ORDER = [
    "01_abstract.md",
    "02_introduction.md",
    "02_related_work_cited.md",
    "03_methods.md",
    "04_detection_model.md",
    "05_results.md",
    "06_discussion.md",
    "07_limitations_ethics.md",
    "08_conclusion.md",
    "09_reproducibility_appendix.md",
]


def assemble_manuscript() -> str:
    section_dir = Path("paper/sections")
    parts: list[str] = []
    for filename in SECTION_ORDER:
        path = section_dir / filename
        parts.append(path.read_text(encoding="utf-8").strip())
    references = Path("paper/references.md").read_text(encoding="utf-8").strip()
    parts.append(references)
    return "\n\n".join(parts) + "\n"


if __name__ == "__main__":
    output_path = Path("paper/manuscript_assembled.md")
    output_path.write_text(assemble_manuscript(), encoding="utf-8")
