import math

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

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        earth_orbits = self.seconds / 31557600
        earth_years = round(earth_orbits, 2)
        return f"Earth years: {earth_years}"

    def on_mercury(self):
        mercury_years = round((self.on_earth() * 0.2408467), 2)
        return f"Mercury years: {mercury_years}"

    def on_venus(self):
        venus_years = round((self.on_earth() * 0.61519726), 2)
        return f"Venus years: {venus_years}"

    def on_mars(self):
        mars_years = round((self.on_earth() * 1.8808158), 2)
        return f"Mars years: {mars_years}"

    def on_jupiter(self):
        jupiter_years = round((self.on_earth() * 11.862615), 2)
        return f"Jupiter years: {jupiter_years}"

    def on_saturn(self):
        saturn_years = round((self.on_earth() * 29.447498), 2)
        return f"Saturn years: {saturn_years}"

    def on_uranus(self):
        uranus_years = round((self.on_earth() * 84.016846), 2)
        return f"Uranus years: {uranus_years}"

    def on_neptune(self):
        neptune_years = round((self.on_earth() * 164.79132), 2)
        return f"Neptune years: {neptune_years}"
