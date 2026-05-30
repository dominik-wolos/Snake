import hashlib
import uuid
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
IDENTITY_FILE = PROJECT_ROOT / ".player_id"


def get_player_identifier() -> str:
    node = uuid.getnode()

    if node and not node & 0x010000000000:
        raw_identifier = f"mac:{node:012x}"
    else:
        raw_identifier = f"local:{_get_local_identifier()}"

    return hashlib.sha256(raw_identifier.encode("utf-8")).hexdigest()[:32]


def _get_local_identifier() -> str:
    if IDENTITY_FILE.exists():
        existing = IDENTITY_FILE.read_text(encoding="utf-8").strip()
        if existing:
            return existing

    generated = uuid.uuid4().hex
    IDENTITY_FILE.write_text(generated, encoding="utf-8")
    return generated
