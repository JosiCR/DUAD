class WebShooter:
    def shoot_web(self):
        print("Im shooting webs from my hands")


class WallClimber:
    def climb_walls(self):
        print("Im climbing a wall like a spider")


class SpiderSense:
    def sense_danger(self):
        print("My spider sense is tingling, theres danger nearby")


class SpiderMan(WallClimber, WebShooter, SpiderSense):
    def introduce(self):
        print("Im Spider-Man your friendly neighborhood hero")

spidey = SpiderMan()

spidey.introduce()
spidey.shoot_web()
spidey.climb_walls()
spidey.sense_danger()