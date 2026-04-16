#!/usr/bin/env python3
import subprocess
import sys

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    open("/Users/laychen/Desktop/AI-SKILL/_git_do.log", "w").write(
        f"CMD: {cmd}\nEXIT: {r.returncode}\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}\n"
    )
    return r.returncode

c = run(
    "cd /Users/laychen/Desktop/AI-SKILL && git add -A && git status && "
    "git commit -m 'Rename skills: haven-yields-scout, haven-evm-wallet' && "
    "git push origin main"
)
sys.exit(c)
