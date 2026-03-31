from shapely.geometry import Point

class SpotGenerator:

    def __init__(self, dump_area, dump_front):
        self.dump_area = dump_area
        self.front = dump_front

        minx, miny, maxx, maxy = dump_area.boundary.bounds
        self.minx = minx + 6
        self.maxx = maxx - 6

        self.spacing = 12
        self.used_spots = []

    # create ONE row only
    def get_all_current_row_spots(self):

        y = self.front.get_active_row()
        row_spots = []

        x = self.minx
        while x <= self.maxx:

            if self.dump_area.is_inside(x, y) and self.is_far(Point(x, y)):
                row_spots.append((x, y))

            x += self.spacing

        # if no space → move front upward
        if not row_spots:
            self.front.advance()
            return self.get_all_current_row_spots()

        return row_spots


    def register_spot(self, spot):
        self.used_spots.append(spot)

        # check if row filled
        if len(self.used_spots) % 5 == 0:
            self.front.advance()


    def is_far(self, point, min_dist=9):
        for sx, sy in self.used_spots:
            if point.distance(Point(sx, sy)) < min_dist:
                return False
        return True