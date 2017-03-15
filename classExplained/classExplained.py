'''
Created on Mar 15, 2017

@author: jackwang
'''
from math import sqrt

class Rocket(object):
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    ROCKET_TYPE = (20, 40, 60, 80)
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        if x == 0 and y == 0:
            self.type = self.ROCKET_TYPE[0]
        elif x > 5 and x < 20:
            self.type = self.ROCKET_TYPE[1]
        elif x > 0 and x <= 5:
            self.type = self.ROCKET_TYPE[2]
        else:
            self.type = self.ROCKET_TYPE[3]
    
    def get_MAXtype(self):
        return self.ROCKET_TYPE[3]
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        
# We have to explicitly pass the arguments NewClass=Shuttle and self when you call super() in Python 2.7. The SpaceShuttle class would look like this:        
        super(Shuttle, self).__init__(x, y)
        self.old_type = self.type
        self.type = super(Shuttle, self).get_MAXtype()
        self.flights_completed = flights_completed
        
shuttleA = Shuttle(10,0,3)
shuttleB = Shuttle(1,2,7)
print(shuttleA)
print(shuttleB)
