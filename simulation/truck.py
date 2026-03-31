import random

class Truck:

    def __init__(self, dump_area, spot_generator):
        self.dump_area = dump_area
        self.generator = spot_generator

        # ENTRY ROAD (all trucks start from same location)
        minx, miny, maxx, maxy = self.dump_area.boundary.bounds

        self.start_x = (minx + maxx) / 2
        self.start_y = miny - 20   # outside dump → haul road

        self.target = self.generator.get_next_spot()

    def path(self):
        if self.target is None:
            return None

        return (self.start_x, self.start_y, self.target[0], self.target[1])