import pyglet
import game.Maps


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(caption="The bug game")
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.key_handler)

        pyglet.clock.schedule_interval(self.tick, 1/20)

        self.world = game.Maps.ActiveWorld()
        self.world.prepare_map("test_map")
        self.world.switch_map("test_map")

    def tick(self, dt: float):
        pass

    def on_draw(self):
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.clear()

        self.world.draw()

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

