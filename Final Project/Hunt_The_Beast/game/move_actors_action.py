from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
   # Description:
    #   Takes the users input from input service and converts it into a action that alters actors or ends 
    #   the game
    # 
    # OOP Principles Used:
    #   Abstraction
    #
    # Reasoning:
    #   This class uses abstraction because it takes the velocity and position and gives actors a new position
    #
    #   It also uses inheritance by inheriting the class action, so when the director executes actions it
    #   will activate this class as well

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        x = (x1 + x2) 
        y = (y1 + y2) 
        position = Point(x, y)
        actor.set_position(position)
    