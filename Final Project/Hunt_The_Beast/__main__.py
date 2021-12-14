import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}
    cast["brick"] = []
    for x in range(7, 100, 7):
        for y in range(3, 30, 6):
            for t in range(0, 3, 1):
                position = Point(x, y + t)
                brick = Actor()
                brick.set_text("|")
                brick.set_position(position)
                cast["brick"].append(brick)
    
    i = 0
    for x in range(7, 100, 14):
        for y in range(2, 30, 4):
            i += 1
            z = 0
            for t in range(0, 8, 1):
                position = Point(x + t, y - (2 * z))
                if i ==3:
                    z += 1
                    i = 0
                brick = Actor()
                brick.set_text("~")
                brick.set_position(position)
                cast["brick"].append(brick)

    
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle = Actor()
    paddle.set_text("===========")
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1)
    ball = Actor()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]

    x = int(constants.MAX_X - 1)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    score = Actor()
    score.set_text(len(cast["brick"]))
    score.set_position(position)
    cast["score"] = [score]
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)