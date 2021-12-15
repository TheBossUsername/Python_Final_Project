from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor
from game.game_over import Game_Over

class ControlActorsAction(Action):
    # Description:
    #   Takes the users input from input service and converts it into a action that alters actors or ends 
    #   the game
    # 
    # OOP Principles Used:
    #   Abstraction
    #
    # Reasoning:
    #   This class uses abstraction because it takes data from the input service and converts it into actions
    #   without having to code it in main
    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        direction = self._input_service.get_direction()
        x1 = direction.get_x()
        y1 = direction.get_y()
        if x1 == -1 or x1 == 1 or y1 == -1 or y1 == 1:
            bow = cast["bow"][0]
            hunter = cast["hunter"][0]
            if x1 == -1:
                bow.set_text("<")
            elif x1 == 1:
                bow.set_text(">")
            elif y1 == -1:
                bow.set_text("^")
            elif y1 == 1:
                bow.set_text("v")
            position = hunter.get_position()
            x = position.get_x()
            y = position.get_y()
            position = Point(x + x1, y + y1)
            bow.set_position(position) 
        elif x1 == 5:
            bow = cast["bow"][0]
            hunter = cast["hunter"][0]
            dragon = cast["dragon"][0]
            arrows = cast["arrows"][0]
            x = arrows.get_value()
            x -= 1
            arrows.set_value(x)
            arrows.set_text(f"Arrows: {arrows.get_value()}")
            bposition = bow.get_position()
            hposition = hunter.get_position()
            dposition = dragon.get_position()
            bx = bposition.get_x()
            by = bposition.get_y()
            hx = hposition.get_x()
            hy = hposition.get_y()
            dx = dposition.get_x()
            dy = dposition.get_y()
            if bx == hx + 1:
                for t in range(12, 80, 14):
                    if dx == hx + t and dy == hy:
                        Game_Over.dragon_killed()
            elif bx == hx - 1:
                for t in range(16, 80, 14):
                    if dx == hx - t and dy == hy:
                        Game_Over.dragon_killed()
            elif by == hy + 1:
                for t in range(6, 30, 6):
                    if dx + 2 == hx and dy == hy + t:
                        Game_Over.dragon_killed()
            elif by == hy - 1:
                for t in range(6, 30, 6):
                    if dx + 2 == hx and dy == hy - t:
                        Game_Over.dragon_killed()
            if arrows.get_value() == 0:
                Game_Over.out_of_arrows()
        else:
            hunter = cast["hunter"][0] 
            hunter.set_velocity(direction)   
            bow = cast["bow"][0] 
            bow.set_velocity(direction)      
