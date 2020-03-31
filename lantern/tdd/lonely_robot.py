class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }
        self.direction = turns[self.direction]

    def move_forward(self):
        if self.direction == "N":
            self.x += 1
        elif self.direction == "S":
            self.x -= 1
        elif self.direction == "E":
            self.y += 1
        else:
            self.y -= 1

    def move_backward(self):
        if self.direction == "N":
            self.x -= 1
        elif self.direction == "S":
            self.x += 1
        elif self.direction == "E":
            self.y -= 1
        else:
            self.y += 1

    def facing_obstacle(self):
       if self.x == self.asteroid.obstacle.obst_x and self.y == self.asteroid.obstacle.obst_y:
           raise CrushIntoObstacleError


class MissAsteroidError(Exception):
    pass


class CrushIntoObstacleError(Exception):
    pass

class ObstacleOutsideAsteroidError(Exception):
    pass