class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return self.seconds / MERCURY_YEAR

    def on_venus(self):
        return self.seconds / VENUS_YEAR

    def on_earth(self):
        return self.seconds / EARTH_YEAR

    def on_mars(self):
        return self.seconds / MARS_YEAR

    def on_jupiter(self):
        return self.seconds / JUPITER_YEAR

    def on_saturn(self):
        return self.seconds / SATURN_YEAR

    def on_uranus(self):
        return self.seconds / URANUS_YEAR

    def on_neptune(self):
        return self.seconds / NEPTUNE_YEAR


MERCURY_YEAR = 0.2408467
VENUS_YEAR = 0.61519726
EARTH_YEAR = 1.0
MARS_YEAR = 1.8808158
JUPITER_YEAR = 11.862615
SATURN_YEAR = 29.447498
URANUS_YEAR = 84.016846
NEPTUNE_YEAR = 164.79132
