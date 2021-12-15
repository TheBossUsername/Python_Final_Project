class Action:
    # Description:
    #   A superclass template that all actions fall under it has an execute function that if subclasses 
    #   don't have it will raise an error
    #
    # OOP Principles Used:
    #   Polymorphism, inheritance
    #
    # Reasoning:
    #   This class uses polymorphism because every action has a execute but depending on the action it may be
    #   different.
    #
    #   It also uses inheritance by giving all it's subclasses the execute funtion which the subclass can fill

    def execute(self, cast):
        raise NotImplementedError("execute not implemented in superclass")