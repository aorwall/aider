import math

class SpaceAge:
    EARTH_YEAR_IN_SECONDS = 31557600
    ORBITAL_PERIOD_FACTORS = {
        "MERCURY": 0.2408467,
        "VENUS": 0.61519726,
        "MARS": 1.8808158,
        "JUPITER": 11.862615,
        "SATURN": 29.447498,
        "URANUS": 84.016846,
        "NEPTUNE": 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return self.get_age_on("MERCURY")

    def on_venus(self):
        return self.get_age_on("VENUS")

    def on_earth(self):
        return self.get_age_on("EARTH")

    def on_mars(self):
        return self.get_age_on("MARS")

    def on_jupiter(self):
        return self.get_age_on("JUPITER")

    def on_saturn(self):
        return self.get_age_on("SATURN")

    def on_uranus(self):
        return self.get_age_on("URANUS")

    def on_neptune(self):
        return self.get_age_on("NEPTUNE")
