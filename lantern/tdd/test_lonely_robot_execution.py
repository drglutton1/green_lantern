import pytest
from lonely_robot import *


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size, robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class TestMoves:

    def setup(self):
        self.x = 10
        self.y = 15
        self.asteroid = Asteroid(self.x, self.y)

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        (
            ("N", "W"),
            ("W", "S"),
            ("S", "E"),
            ("E", "N")
        )
    )
    def test_turns_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        (
            ("N", "E"),
            ("E", "S"),
            ("S", "W"),
            ("W", "N")
        )
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "direction, current_x, current_y, expected_x, expected_y",
        (
                ("N", 5, 4, 6, 4),
                ("E", 8, 6, 8, 7),
                ("S", 9, 3, 8, 3),
                ("W", 7, 5, 7, 4)
        )
    )
    def test_move_forward(self, direction, current_x, current_y, expected_x, expected_y):
        robot = Robot(current_x, current_y, self.asteroid, direction)
        robot.move_forward()
        assert robot.x == expected_x
        assert robot.y == expected_y

    @pytest.mark.parametrize(
        "direction, current_x, current_y, expected_x, expected_y",
        (
                ("N", 8, 5, 7, 5),
                ("E", 5, 6, 5, 5),
                ("S", 10, 9, 11, 9),
                ("W", 4, 10, 4, 11)
        )
    )
    def test_move_backward(self, direction, current_x, current_y, expected_x, expected_y):
        robot = Robot(current_x, current_y, self.asteroid, direction)
        robot.move_backward()
        assert robot.x == expected_x
        assert robot.y == expected_y



