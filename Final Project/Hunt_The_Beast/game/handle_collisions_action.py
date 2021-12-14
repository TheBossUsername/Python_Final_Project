import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        score = cast["score"]
        
        ball_position = ball.get_position()
        ball_velocity = ball.get_velocity()
        paddle_postion = paddle.get_position()
        #I would break these two if statements into different classes
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                hit_brick = bricks.index(brick)
                bricks.pop(hit_brick)
                clunk = ball_velocity.reverse_y()
                ball.set_velocity(clunk)
                x = int(constants.MAX_X - 1)
                y = int(constants.MAX_Y - 1)
                position = Point(x, y)
                score = Actor()
                score.set_text(len(cast["brick"]))
                score.set_position(position)
                cast["score"] = [score]


        if ball_position.get_x() == 2 or ball_position.get_x() == constants.MAX_X - 2:
            clunk = ball_velocity.reverse_x()
            ball.set_velocity(clunk)

        if ball_position.get_y() == 2:
            
            clunk = ball_velocity.reverse_y()
            ball.set_velocity(clunk)

        if paddle_postion.get_y() - 2 == ball_position.get_y():
            min_x = paddle_postion.get_x()
            max_x = min_x + len(paddle.get_text())
            if ball_position.get_x() >= min_x and ball_position.get_x() <= max_x:
                clunk = ball_velocity.reverse_y()
                ball.set_velocity(clunk) 
