"""In-memory index store used for early scaffolding and tests."""


class IndexStore:
    """Simple in-memory store for chunks and embeddings."""

    def __init__(self) -> None:
        self.records: list[dict] = []

    def add(self, record: dict) -> None:
        self.records.append(record)

    def all(self) -> list[dict]:
        return list(self.records)
