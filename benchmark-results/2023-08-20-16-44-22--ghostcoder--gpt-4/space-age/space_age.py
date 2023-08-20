class SpaceAge:
    EARTH_YEAR_SECONDS = 31557600
    ORBITAL_PERIODS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = self.seconds / self.EARTH_YEAR_SECONDS

    def on_mercury(self):
        return self.earth_years / self.ORBITAL_PERIODS['mercury']

    def on_venus(self):
        return self.earth_years / self.ORBITAL_PERIODS['venus']

    def on_earth(self):
        return self.earth_years / self.ORBITAL_PERIODS['earth']

    def on_mars(self):
        return self.earth_years / self.ORBITAL_PERIODS['mars']

    def on_jupiter(self):
        return self.earth_years / self.ORBITAL_PERIODS['jupiter']

    def on_saturn(self):
        return self.earth_years / self.ORBITAL_PERIODS['saturn']

    def on_uranus(self):
        return self.earth_years / self.ORBITAL_PERIODS['uranus']

    def on_neptune(self):
        return self.earth_years / self.ORBITAL_PERIODS['neptune']