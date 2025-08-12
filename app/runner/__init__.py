import subprocess, tempfile, os
from pathlib import Path
from flask import current_app

def _compiler_cmd(src: Path, out: Path):
    cfg = current_app.config["RUNNER_CFG"]
    if cfg["COMPILER"] == "tcc":
        return [cfg["TCC_PATH"], str(src), "-o", str(out)]
    return [cfg["GCC_PATH"], str(src), "-o", str(out)]

def compile_and_run(lesson_dir: Path, user_input: str = ""):
    src = lesson_dir / "program.c"
    if not src.exists():
        return False, "", "program.c not found"
    
    with tempfile.TemporaryDirectory() as tmpdir:
        exe_path = Path(tmpdir, "a.exe" if os.name == "nt" else "a.out")

        try:
            compile_proc = subprocess.run(
                _compiler_cmd(src, exe_path),
                capture_output=True, text=True, timeout=10
            )
        except FileNotFoundError:
            return False, "", "Compiler not found in tools"
        except subprocess.TimeoutExpired:
            return False, "", "Compile timeout"
        
        if compile_proc.returncode != 0:
            return False, "", compile_proc.stderr
        
        try:
            run_proc = subprocess.run(
                [str(exe_path)],
                input=(user_input or "") + "\n",
                capture_output=True, text=True,
                timeout=current_app.config["RUNNER_CFG"]["TIMEOUT_SEC"]
            )
        except subprocess.TimeoutExpired:
            return False, "", "Program exceeded time limit"
        
        return (run_proc.returncode == 0), run_proc.stdout, run_proc.stderr