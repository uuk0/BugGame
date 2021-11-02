import pyglet


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(caption="The bug game")
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.key_handler)

        pyglet.clock.schedule_interval(self.tick, 1/20)

    def tick(self, dt: float):
        pass

    def on_draw(self):
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.clear()

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

