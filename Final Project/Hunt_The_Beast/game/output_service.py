import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    # Description:
    #   It takes the text and position of the actors and prints them to the screen
    # 
    # OOP Principles Used:
    #   None that I can think of
    #
    # Reasoning:
    #   None that I can think of

    def __init__(self, screen):
        self._screen = screen
        
    def clear_screen(self):
        self._screen.clear_buffer(7, 0, 0)
        
    def draw_actor(self, actor):
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y)

    def draw_actors(self, actors):
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        self._screen.refresh()    