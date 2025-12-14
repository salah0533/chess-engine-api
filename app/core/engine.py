import platform
import os
from stockfish import Stockfish

CORE_DIR = os.path.dirname(os.path.abspath(__file__))


# project_root
PROJECT_ROOT = os.path.abspath(os.path.join(CORE_DIR, ".."))

def get_stockfish_path() -> str:
    system = platform.system().lower()

    if system == "linux":
        path = os.path.join(PROJECT_ROOT, "engines", "linux", "stockfish-ubuntu-x86-64-avx2")

    elif system == "windows":
        path = os.path.join(PROJECT_ROOT, "engines", "windows", "stockfish-windows-x86-64-avx2.exe")

    else:
        raise RuntimeError(f"Unsupported OS: {system}")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Stockfish binary not found: {path}")

    return os.path.abspath(path)


engine = Stockfish(
        path=get_stockfish_path(),
        depth=15,
        parameters={"Threads": 1}
    )
