#!/usr/bin/env python3
import traceback

import tcod

import color
import exceptions
import input_handlers
import setup_game


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine, then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def create_main_menu():
    return setup_game.MainMenu()


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    handler: input_handlers.BaseEventHandler = create_main_menu()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Python Game Guys",
        vsync = True,
    ) as context:
        # The order parameter sets numpy to use [x,y] instead of [y,x] format.
        root_console = tcod.Console(screen_width, screen_height, order = "F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)

                    if isinstance(handler, input_handlers.GameOverEventHandler):
                        # The player was killed sometime while handling events
                        handler.set_create_main_menu_function(create_main_menu)

                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()