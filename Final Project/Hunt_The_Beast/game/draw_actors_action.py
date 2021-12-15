from game.action import Action

class DrawActorsAction(Action):
    # Description:
    #   It takes the cast and script of all the actors and actions and runs the game
    # 
    # OOP Principles Used:
    #   Inheritance
    #
    # Reasoning:
    #   It uses inheritance by inheriting the class action, so when the director executes actions it
    #   will activate this class as well
    def __init__(self, output):
        super().__init__()
        self._output = output
    
    def execute(self, cast):
        self._output.clear_screen()
        for group in cast.values():
            self._output.draw_actors(group)
        self._output.flush_buffer()