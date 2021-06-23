#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    screen_width=80
    screen_height=50

    map_width=40
    map_height=40

    tileset=tcod.console_set_custom_font('alloy.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_CP437, 16, 16)


    event_handler=EventHandler()

    player=Entity(int(5), int(5), "@", (222, 238, 214))
    entities={player}

    game_map=generate_dungeon(10,map_width,map_height)
    engine=Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="WOLF TOWER",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events=tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()