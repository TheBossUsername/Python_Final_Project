from game import constants
from game.point import Point

class Actor:
#
# Description:
#   A visible, moveable thing that participates in the game. 
#   The responsibility of Actor is to keep track of its appearance, position, value 
#   and velocity in 2d space.
#
# OOP Principles Used:
#   Encapsulation, Polymorphism
#
# Reasoning:
#   This class uses encapsulation becuase there is functions to set and get attributes of actors but no way 
#   manually change the data inside 
#

    def __init__(self):
        """The class constructor."""
        self._description = ""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_description(self):
        """Gets the artifact's description.
        
        Returns:
            string: The artifact's description.
        """
        return self._description 

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def get_value(self):
        """Updates the actor's text to the given value.
        
        Args:
            value (int): The given value.
        """
        return self._value
    
    def set_description(self, description):
        """Updates the actor's description to the given one.
        
        Args:
            description (string): The given description.
        """
        self._description = description

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text
    
    def set_value(self, value):
        """Updates the actor's text to the given value.
        
        Args:
            value (int): The given value.
        """
        self._value = value

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity
    
    def set_tag(self, tag):
        self._tag = tag
    