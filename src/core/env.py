from dotenv import load_dotenv

load_dotenv()

import os

from pathlib import Path

SCR_DIR = Path(__file__).resolve().parent.parent  # src

INSTRUCTIONS_DIR = SCR_DIR / "agents" / "instructions"  # src/agents/instructions

DOCS_DIR = SCR_DIR / "docs"  # src/docs

OUTPUT_DIR = SCR_DIR / "output"  # src/output

def _required_env(name: str) -> str:
    """Ambil env wajib. apabila gagal, tampilkan pesan error"""

    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"env variabel `{name}` belum di-set")

    return value

GEMINI_API_KEY = _required_env("GEMINI_API_KEY")
GEMINI_MODEL = _required_env("GEMINI_MODEL")
GEMINI_MODEL_TTS = _required_env("GEMINI_MODEL_TTS")

SUPABASE_URL = _required_env("SUPABASE_URL")
SUPABASE_KEY = _required_env("SUPABASE_KEY")