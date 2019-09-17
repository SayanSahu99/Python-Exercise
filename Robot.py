class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def movement(self, steps, up, down , left, right):
        if up:
            self.x += int(steps)

        elif down:
            self.x -= int(steps)

        elif left:
            self.y -= int(steps)

        elif right:
            self.y += int(steps)

    def destination(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return int(distance)

robo = Robot()
print('''Controls Of The Robot:
         Type: (PRESS 1 TO STOP)

         UP distance
         RIGHT distance
         LEFT distance
         DOWN distance

         ''')

control = input()
control = control.split(' ')
up, down, left, right =False, False, False, False
while control[0] != '1':
    if control[0] == 'UP' or control[0] == 'up':
        up = True
        robo.movement(control[1], up, down, left, right)
        up = False

    elif control[0] == 'DOWN' or control[0] == 'down' :
        down = True
        robo.movement(control[1], up, down, left, right)
        down = False

    elif control[0] == 'LEFT' or control[0] == 'left':
        left = True
        robo.movement(control[1], up, down, left, right)
        left = False

    elif control[0] == 'RIGHT' or control[0] == 'right':
        right = True
        robo.movement(control[1], up, down, left, right)
        right = False

    control = input()
    control = control.split()

print()
print('Distance of the robot from original position : ' + str(robo.destination()) + ' units')
