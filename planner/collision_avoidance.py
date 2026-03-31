from shapely.geometry import Point
import math

class CollisionAvoidance:

    def __init__(self):
        self.recent_spots = []

    # small shift if trucks are too close
    def make_safe(self, spot):

        if spot is None:
            return None

        x, y = spot
        point = Point(x, y)

        for sx, sy in self.recent_spots:
            dist = point.distance(Point(sx, sy))

            # if trucks too close → shift sideways
            if dist < 6:
                angle = math.radians(30)
                x = x + 3 * math.cos(angle)
                y = y + 3 * math.sin(angle)
                point = Point(x, y)

        self.recent_spots.append((x, y))

        # keep only last 8 trucks in memory
        if len(self.recent_spots) > 8:
            self.recent_spots.pop(0)

        return (x, y)