from shapely.geometry import Polygon, Point

class DumpArea:

    def __init__(self):
        self.boundary = Polygon([
            (0,0),
            (150,0),
            (170,40),
            (130,90),
            (80,120),
            (30,100),
            (0,40)
        ])

    # IMPORTANT: self MUST be first parameter
    def is_inside(self, x, y):
        return self.boundary.contains(Point(float(x), float(y)))