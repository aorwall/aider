class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return self.seconds / 0.2408467

    def on_venus(self):
        return self.seconds / 0.61519726

    def on_earth(self):
        return self.seconds / 1.0

    def on_mars(self):
        return self.seconds / 1.8808158

    def on_jupiter(self):
        return self.seconds / 11.862615

    def on_saturn(self):
        return self.seconds / 29.447498

    def on_uranus(self):
        return self.seconds / 84.016846

    def on_neptune(self):
        return self.seconds / 164.79132
