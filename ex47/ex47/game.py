from __future__ import annotations


class Room:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.paths: dict[str, Room] = {}

    def go(self, direction) -> Room | None:
        return self.paths.get(direction, None)

    def add_paths(self, paths) -> None:
        self.paths.update(paths)
