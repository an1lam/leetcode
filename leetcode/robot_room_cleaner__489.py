# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#    """

class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
    
    @property
    def move(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    
UP = Direction(0, -1)
RIGHT = Direction(1, 0)
DOWN = Direction(0, 1)    
LEFT = Direction(-1, 0)

UP.next = RIGHT
RIGHT.next = DOWN
DOWN.next = LEFT
LEFT.next = UP

UP.prev = LEFT
RIGHT.prev = UP
DOWN.prev = RIGHT
LEFT.prev = DOWN


class RobotDriver:
    
    def __init__(self, robot, current_dir=UP, current_pos=(0, 0)):
        self.robot = robot
        self.current_dir = current_dir
        self.current_pos = current_pos
    
    def clean(self):
        self.robot.clean()
    
    def move(self):
        moved = self.robot.move()
        if moved: 
            self.current_pos = (
                self.current_pos[0] + self.current_dir.move[0], 
                self.current_pos[1] + self.current_dir.move[1]
            ) 
        return moved

        
    def turnRight(self):
        self.current_dir = self.current_dir.next
        self.robot.turnRight()

    def turnLeft(self):
        self.current_dir = self.current_dir.prev
        self.robot.turnLeft()
        
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self._clean_room(RobotDriver(robot), set())
    
    def _clean_room(cls, robot, visited):
        if robot.current_pos not in visited:
            print("clean:", robot.current_pos)
            robot.clean()
            visited.add(robot.current_pos) 
            
            for _ in range(4):
                if robot.move():
                    # Assumption is robot always ends where he started facing the opposite direction
                    # he was sent in (in the recursive call).
                    cls._clean_room(robot, visited)
                    robot.move()
                    robot.turnLeft()
                else:
                    robot.turnRight()
        
        robot.turnRight()
        robot.turnRight()

