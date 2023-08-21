class SpaceAge:
    EARTH_YEAR_SECONDS = 31557600
    PLANET_YEARS = {
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
        self.earth_years = seconds / self.EARTH_YEAR_SECONDS

    def on_mercury(self):
        return round(self.earth_years / self.PLANET_YEARS['mercury'], 2)

    def on_venus(self):
        return round(self.earth_years / self.PLANET_YEARS['venus'], 2)

    def on_earth(self):
        return round(self.earth_years, 2)

    def on_mars(self):
        return round(self.earth_years / self.PLANET_YEARS['mars'], 2)

    def on_jupiter(self):
        return round(self.earth_years / self.PLANET_YEARS['jupiter'], 2)

    def on_saturn(self):
        return round(self.earth_years / self.PLANET_YEARS['saturn'], 2)

    def on_uranus(self):
        return round(self.earth_years / self.PLANET_YEARS['uranus'], 2)

    def on_neptune(self):
        return round(self.earth_years / self.PLANET_YEARS['neptune'], 2)
