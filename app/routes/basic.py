from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required
from pathlib import Path
import yaml
import socket
from ..runner import compile_and_run, run_code
from ..config import current_cfg as cfg

bp = Blueprint('basic', __name__)


def load_lesson(lesson_dir: Path):
    with open(lesson_dir / "lesson.yaml", "r", encoding="utf-8") as f:
        meta = yaml.safe_load(f)
    return meta


def lessons_list():
    items = []
    for p in sorted(cfg.LESSONS_PATH.iterdir()):
        if (p / "lesson.yaml").exists():
            meta = load_lesson(p)
            items.append({"slug": p.name, "title": meta["title"], "summary": meta.get("summary", "")})
    return items


def _lan_ip():
    ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        try:
            s.close()
        except Exception:
            pass
    return ip


@bp.route("/")
def index():
    try:
        port = request.host.split(":")[1]
    except Exception:
        port = str(current_app.config.get("FLASK_RUN_PORT") or 7777)

    ip_only = _lan_ip()
    full_host = f"{ip_only}:{port}"  # if you still need it
    return render_template("index.html", ip_only=ip_only, full_host=full_host, port=port)


@bp.route("/lessons")
@login_required
def lessons():
    return render_template("lessons.html", lessons=lessons_list())


@bp.route("/lesson/<slug>", methods=["GET", "POST"])
@login_required
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

@bp.route("/playground", methods=["GET", "POST"])
@login_required
def playground():
    if request.method == "POST":
        user_input = request.form.get("code", "")
        retcode, output, errors = run_code(user_input)
        return render_template("playground.html", 
                               retcode=retcode, output=output, errors=errors)
    
    return render_template("playground.html")