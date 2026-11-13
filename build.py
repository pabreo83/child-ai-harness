"""나뉜 파일을 합쳐 dist/HARNESS_ALL.md를 만듭니다. 사용: python build.py"""
from pathlib import Path
root = Path(__file__).parent
order = ["HARNESS.md",
         "situations/risk.md", "situations/restrictions.md", "situations/tools.md",
         "situations/worries.md", "situations/privacy.md", "situations/learning.md",
         "situations/wellbeing.md",
         "age/elementary.md", "age/middle.md", "age/high.md"]
parts = []
for f in order:
    t = (root / f).read_text(encoding="utf-8").strip()
    if f != "HARNESS.md":
        lines = t.splitlines()
        lines[0] = "## " + lines[0].lstrip("# ") + f"  (`{f}`)"
        t = "\n".join(("#" + l) if l.startswith("## ") and i else l for i, l in enumerate(lines))
    parts.append(t)
(root / "dist").mkdir(exist_ok=True)
(root / "dist/HARNESS_ALL.md").write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
print("dist/HARNESS_ALL.md 생성 완료")
