class Band(object):

    def __init__(self):
        self("")

    def __init__(self, name, band_id=100):
        self.name = name
        self.band_id = band_id

    def __str__(self):
        return "Name: {0}, id: {1}".format(self.name, self.band_id)

    def set_name(self, name):
        self.name = name


band = Band("dango")
band2 = Band("Oren")


print(band)
print(band2)

band.set_name("Where is my mind")
print(band.name)
