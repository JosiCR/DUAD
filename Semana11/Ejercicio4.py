class Head: 
    def __init__(self):
        self.eyes = 2
        self.mouth = 1


class Hand:
    def __init__(self, side):
        self.fingers = 5
        self.side = side


class Arm:
    def __init__(self, side):
        self.hand = Hand(side)
        self.side = side


class Leg:
    def __init__(self, side):
        self.foot = Foot(side)
        self.side = side


class Foot:
    def __init__(self, side):
        self.toes = 2
        self.side = side


class Torso:
    def __init__(self, Head, right_arm, left_arm, right_leg, left_leg):
        self.Head = Head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Human :
    def __init__ (self, torso):
        self.torso = torso


Head = Head()

left_Hand = Hand("Left")
Right_Hand = Hand("Right")
left_arm = Arm("Left")
Right_arm = Arm("Right")
left_leg = Leg("Left")
Right_leg = Leg("Right")

torso = Torso(Head, left_arm, Right_arm, left_leg, Right_leg)
human = Human(torso)
