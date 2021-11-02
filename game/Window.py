import math
import sys
import traceback

import pyglet
from pyglet.window import key
import game.Maps
from game import Stats


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(caption="The bug game")
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.key_handler)

        pyglet.clock.schedule_interval(self.tick, 1/20)

        self.world = game.Maps.ActiveWorld()
        self.world.prepare_map("test_map")
        self.world.switch_map("test_map")

        self.disclaimer_lines = [
            "This game is about BUGS",
            "Not the real life ones, but software bugs",
            "Don't report bugs if they are not game-breaking",
            "Use them for your advantage!",
            "(Maybe you need to use bugs in order to complete the game...)"
        ]
        self.disclaimer_timeout = 3
        self.max_disclaimer_timeout = 3
        self.disclaimer_fade_function = lambda dt: round(math.cos(abs(dt - .5) * math.pi) * 255)
        self.disclaimer_lable = pyglet.text.Label(text="DISCLAIMER", color=(255, 0, 0, 255), font_size=30, multiline=True, width=600)

        self.current_draw_stack = [self.draw_disclaimer]

    def draw_disclaimer(self):
        wx, wy = self.get_size()
        sx, sy = self.disclaimer_lable.content_width, self.disclaimer_lable.content_height
        self.disclaimer_lable.position = 20, wy - 10 - sy

        self.disclaimer_lable.color = (255, 0, 0, self.disclaimer_fade_function(self.disclaimer_timeout / self.max_disclaimer_timeout))

        self.disclaimer_lable.draw()

    def tick(self, dt: float):
        if self.disclaimer_timeout > 0:
            self.disclaimer_timeout -= dt
            if self.disclaimer_timeout <= 0:
                if self.disclaimer_lines:
                    self.disclaimer_lable.text = self.disclaimer_lines.pop(0)
                    self.disclaimer_timeout = self.max_disclaimer_timeout
                else:
                    self.current_draw_stack.remove(self.draw_disclaimer)

    def on_draw(self):
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.clear()

        self.world.draw()

        for draw_handler in self.current_draw_stack:
            draw_handler()

    def on_key_press(self, symbol, modifiers):
        if self.disclaimer_timeout > 0 and symbol == key.ESCAPE:
            traceback.print_exception(RuntimeError("Internal processing error: Property 'EscapeAction' is not set!"))

            Stats.TRIGGERED_BUGS += 1
            Stats.COLLECTED_BUGS.add("startup:esc_crash")
            Stats.save()

            self.close()
            pyglet.app.exit()

    def on_key_release(self, symbol, modifiers):
        pass

