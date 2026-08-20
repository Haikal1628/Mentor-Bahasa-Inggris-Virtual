import src.core.env as env

from functools import lru_cache
from supabase import Client, create_client


@lru_cache
def load_instruction(name: str):
    """Baca file instruksi berdasarkan nama file, contoh: load_instruction('agent-lead')"""

    path = env.INSTRUCTIONS_DIR / f"{name}.md"  # src/agents/instructions/agent-lead.md

    if not path.exists():
        raise FileNotFoundError(
            f"File instruksi tidak ditemukan: {path}. \n"
            f"Cek nama file di {env.INSTRUCTIONS_DIR}"
        )  # agent-lead, agent-led

    return path.read_text(encoding="utf-8")

# saat memanngil load_instruction("agent-lead") kenapa tidak perlu menulis .mdnya misal agent-lead.md, karena di dalam fungsi load_instruction sudah ditambahkan ekstensi .md pada path file instruksi. Jadi cukup menulis nama file tanpa ekstensi .md, dan fungsi akan otomatis menambahkan ekstensi tersebut saat mencari file instruksi.