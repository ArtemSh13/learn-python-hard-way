from ex47.game import Room


def test_room():
    gold = Room(
        "GoldRoom",
        """В этой комнате полно золота, которое можно украсть.
                Здесь есть дверь с выходом на север.""",
    )
    assert gold.name == "GoldRoom"
    assert gold.paths == {}


def test_room_paths():
    center = Room("Center", "Тестирование центральной комнаты.")
    north = Room("North", " Тестирование северной комнаты.")
    south = Room("South", " Тестирование южной комнаты.")

    center.add_paths({"north": north, "south": south})
    assert center.go("north") == north
    assert center.go("south") == south


def test_map():
    start = Room("Start", "Вы можете идти на запад и провалиться в яму.")
    west = Room("Trees", "Здесь есть деревья и вы можете отправиться на восток.")
    down = Room("Dungeon", "Здесь темно и вы можете подняться вверх.")

    start.add_paths({"west": west, "down": down})
    west.add_paths({"east": start})
    down.add_paths({"up": start})

    assert start.go("west") == west
    assert start.go("west").go("east") == start  # pyright: ignore[reportOptionalMemberAccess]
    assert start.go("down").go("up") == start  # pyright: ignore[reportOptionalMemberAccess]
