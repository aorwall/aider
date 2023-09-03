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


def test_age_on_earth():
    age = SpaceAge(1000000000)
    assert age.on_earth() == 31.69

def test_age_on_jupiter():
    age = SpaceAge(901876382)
    assert age.on_jupiter() == 2.41

def test_age_on_mars():
    age = SpaceAge(2129871239)
    assert age.on_mars() == 35.88

def test_age_on_mercury():
    age = SpaceAge(2134835688)
    assert age.on_mercury() == 280.88

def test_age_on_neptune():
    age = SpaceAge(1821023456)
    assert age.on_neptune() == 0.35

def test_age_on_saturn():
    age = SpaceAge(2000000000)
    assert age.on_saturn() == 2.15
