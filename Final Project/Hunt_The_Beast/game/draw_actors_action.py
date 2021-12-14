from game.action import Action

# TODO: Define the DrawActorsAction class here
class DrawActorsAction(Action):
    def __init__(self, output):
        super().__init__()
        self._output = output
    
    def execute(self, cast):
        self._output.clear_screen()
        for group in cast.values():
            self._output.draw_actors(group)
        self._output.flush_buffer()