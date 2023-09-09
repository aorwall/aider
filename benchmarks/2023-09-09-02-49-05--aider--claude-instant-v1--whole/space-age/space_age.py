class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        earth_years = self.seconds / 31557600
        return round(earth_years, 2)

    def on_mercury(self):
        mercury_years = (self.seconds / 31557600) * 0.2408467
        return round(mercury_years, 2)

    def on_venus(self):
        venus_years = (self.seconds / 31557600) * 0.61519726
        return round(venus_years, 2)

    def on_mars(self):
        mars_years = (self.seconds / 31557600) * 1.8808158
        return round(mars_years, 2)

    def on_jupiter(self):
        jupiter_years = (self.seconds / 31557600) * 11.862615
        return round(jupiter_years, 2)

    def on_saturn(self):
        saturn_years = (self.seconds / 31557600) * 29.447498
        return round(saturn_years, 2)

    def on_uranus(self):
        uranus_years = (self.seconds / 31557600) * 84.016846
        return round(uranus_years, 2)

    def on_neptune(self):
        neptune_years = (self.seconds / 31557600) * 164.79132
        return round(neptune_years, 2)
