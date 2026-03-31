from planner.collision_avoidance import CollisionAvoidance

class SpotAllocator:

    def __init__(self, generator):
        self.generator = generator
        self.collision = CollisionAvoidance()
        self.current_row_queue = []

    def assign_truck(self, truck_id, truck_pos):

        # If queue empty → ask generator for row
        if not self.current_row_queue:
            self.current_row_queue = self.generator.get_all_current_row_spots()

            # dump finished
            if not self.current_row_queue:
                return None

        # FIFO assign
        spot = self.current_row_queue.pop(0)

        # mark used
        self.generator.register_spot(spot)

        # safety adjust
        return self.collision.make_safe(spot)