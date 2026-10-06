import time
import uuid
from datetime import datetime, timezone

INTERVAL = 5  # seconds


def timestamp() -> str:
    """Current UTC time in ISO 8601, e.g. 2020-03-30T12:15:17.705Z"""
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def main() -> None:
    # Generated once on startup and kept in memory.
    stored = str(uuid.uuid4())

    while True:
        print(f"{timestamp()}: {stored}", flush=True)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
