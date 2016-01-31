import os
import subprocess

def test_freefempp():
    """Try running the FreeFem++ interpreter"""
    try:
        with open(os.devnull, "w") as f:
            subprocess.call("FreeFem++", stdout=f)
    except Exception:
        raise Exception("Error when running the FreeFem++ interpreter")
