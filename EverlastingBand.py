from Band import Band
import datetime


class EverlastingBand(Band):

    def __init__(self, name):
        self.when_do_we_start = datetime.datetime.now()
        super(EverlastingBand, self).__init__(name)
