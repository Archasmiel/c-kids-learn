from flask import Blueprint, render_template, request, redirect, url_for, current_app
from pathlib import Path
import yaml
from .runner import compile_and_run

bp = Blueprint("basic", __name__)

def load_lesson(lesson_dir: Path):
    with open(lesson_dir / "lesson.yaml", "r", encoding="utf-8") as f:
        meta = yaml.safe_load(f)
    return meta

def lessons_list():
    base = Path(current_app.root_path).parent / "lessons"
    items = []
    for p in sorted(base.iterdir()):
        if (p / "lesson.yaml").exists():
            meta = load_lesson(p)
            items.append({"slug": p.name, "title": meta["title"], "summary": meta.get("summary", "")})
    return items

@bp.route("/")
def index():
    return render_template("index.html", lessons=lessons_list())

@bp.route("/lesson/<slug>", methods=["GET", "POST"])
def lesson(slug):
    base = Path(current_app.root_path).parent / "lessons" / slug
    meta = load_lesson(base)

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        ok, output, errors = compile_and_run(base, user_input=user_input)
        return render_template("result.html", 
                               ok=ok, output=output, errors=errors, 
                               meta=meta, slug=slug)
    
    return render_template("lesson.html", meta=meta, slug=slug)