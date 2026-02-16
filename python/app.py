from fastapi import HTTPException
from pydantic import BaseModel
from pathlib import Path
import subprocess

class RunReq(BaseModel):
    script: str
    args: list[str] = []

SCRIPTS_DIR = Path("/files/scripts").resolve()

@app.post("/run")
def run(req: RunReq):
    script_path = (SCRIPTS_DIR / req.script).resolve()

    # nur /files/scripts und nur .py erlauben
    if not str(script_path).startswith(str(SCRIPTS_DIR)):
        raise HTTPException(400, "invalid path")
    if not script_path.exists() or script_path.suffix != ".py":
        raise HTTPException(404, "script not found")

    res = subprocess.run(
        ["python", str(script_path), *req.args],
        capture_output=True,
        text=True,
        timeout=600,
    )

    return {
        "returncode": res.returncode,
        "stdout": res.stdout[-4000:],
        "stderr": res.stderr[-4000:],
    }
