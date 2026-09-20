from __future__ import annotations


class Room:
    def __init__(self, name, description) -> None:
        """Initialize a room with specific name and description.

        >>> gold = Room("GoldRoom", "В этой комнате полно золота, которое можно украсть. Здесь есть дверь с выходом на север.")
        >>> gold.name
        'GoldRoom'
        >>> gold.paths
        {}
        """
        self.name = name
        self.description = description
        self.paths: dict[str, Room] = {}

    def go(self, direction) -> Room | None:
        """Move the scene to corresponding room.

        >>> center = Room("Center", "Тестирование центральной комнаты.")
        >>> north = Room("North", " Тестирование северной комнаты.")
        >>> south = Room("South", " Тестирование южной комнаты.")
        >>> center.add_paths({"north": north, "south": south})
        >>> center.go("north") == north
        True
        >>> center.go("south") == south
        True
        """

        return self.paths.get(direction, None)

    def add_paths(self, paths) -> None:
        """Add new path to the room.

        >>> start = Room("Start", "Вы можете идти на запад и провалиться в яму.")
        >>> west = Room("Trees", "Здесь есть деревья и вы можете отправиться на восток.")
        >>> down = Room("Dungeon", "Здесь темно и вы можете подняться вверх.")
        >>> start.add_paths({"west": west, "down": down})
        >>> west.add_paths({"east": start})
        >>> down.add_paths({"up": start})
        >>> start.go("west") == west
        True
        >>> start.go("west").go("east") == start
        True
        >>> start.go("down").go("up") == start
        True
        """
        self.paths.update(paths)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
