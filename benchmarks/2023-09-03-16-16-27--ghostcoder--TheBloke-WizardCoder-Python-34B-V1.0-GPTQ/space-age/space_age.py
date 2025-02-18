class SpaceAge:
    PLANETS = {
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Earth': 1.0,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    SECONDS_IN_EARTH_YEAR = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / self.SECONDS_IN_EARTH_YEAR, 2)


    def on_mercury(self):
        return round((self.seconds / self.SECONDS_IN_EARTH_YEAR) / self.PLANETS['Mercury'], 2)


    def on_venus(self):
        return round((self.seconds / self.SECONDS_IN_EARTH_YEAR) / self.PLANETS['Venus'], 2)

    def on_mars(self):
        return round((self.seconds / self.SECONDS_IN_EARTH_YEAR) / self.PLANETS['Mars'], 2)

    def on_jupiter(self):
        return round((self.seconds / self.SECONDS_IN_EARTH_YEAR) / self.PLANETS['Jupiter'], 2)

    def on_uranus(self):
        return round((self.seconds / self.SECONDS_IN_EARTH_YEAR) / self.PLANETS['Uranus'], 2)

    def on_neptune(self):
        return round((self.seconds / self.SECONDS_IN_EARTH_YEAR) / self.PLANETS['Neptune'], 2)

    def on_saturn(self):
        return round((self.seconds / self.SECONDS_IN_EARTH_YEAR) / self.PLANETS['Saturn'], 2)
