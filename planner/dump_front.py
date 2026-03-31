class DumpFront:

    def __init__(self, dump_area):
        self.dump_area = dump_area

        # polygon bounds
        minx, miny, maxx, maxy = dump_area.boundary.bounds

        self.top = maxy - 5
        self.bottom = miny + 5

        self.row_height = 8  # truck layer height
        self.current_y = self.top

        self.dumps_in_row = 0
        self.max_dumps_per_row = 12   # approx row capacity

    # return ACTIVE dumping layer
    def get_active_row(self):
        return float(self.current_y)

    # called every time truck dumps
    def register_dump(self):
        self.dumps_in_row += 1

        if self.dumps_in_row >= self.max_dumps_per_row:
            self.advance()

    # move to next layer
    def advance(self):
        self.current_y -= self.row_height
        self.dumps_in_row = 0

        if self.current_y < self.bottom:
            self.current_y = self.bottom