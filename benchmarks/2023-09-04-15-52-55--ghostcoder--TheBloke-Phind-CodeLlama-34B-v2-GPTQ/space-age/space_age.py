class SpaceAge:
    EARTH_YEAR_IN_SECONDS = 31557600
    ORBITAL_PERIOD_FACTORS = {
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Earth": 1.0,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Mercury"]

    def on_venus(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Venus"]

    def on_earth(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Earth"]

    def on_mars(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Mars"]

    def on_jupiter(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Jupiter"]

    def on_saturn(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Saturn"]

    def on_uranus(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Uranus"]

    def on_neptune(self):
        years_on_earth = self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS
        return years_on_earth / SpaceAge.ORBITAL_PERIOD_FACTORS["Neptune"]
