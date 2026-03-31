from planner.dump_polygon import DumpArea
from planner.dump_front import DumpFront
from planner.spot_generator import SpotGenerator
from planner.spot_allocator import SpotAllocator

import matplotlib.pyplot as plt

# -----------------------------
# Create dump environment
# -----------------------------
area = DumpArea()
front = DumpFront(area)
generator = SpotGenerator(area, front)
allocator = SpotAllocator(generator)

# Example truck start positions
truck_starts = [
    (0,0),
    (150,0),
    (75,130),
    (30,60),
    (120,70),
    (50,20),
    (90,110),
    (10,40),
    (140,30),
    (60,90)
]

assigned = []

# -----------------------------
# Assign trucks
# -----------------------------
for i,pos in enumerate(truck_starts):
    spot = allocator.assign_truck(i,pos)
    if spot:
        assigned.append((pos,spot))

# -----------------------------
# Plot dump boundary
# -----------------------------
x,y = area.boundary.exterior.xy
plt.figure(figsize=(7,7))
plt.plot(x,y)
plt.fill(x,y, alpha=0.2)

# -----------------------------
# Plot trucks & dump spots
# -----------------------------
for start,end in assigned:
    plt.scatter(start[0],start[1],color="green",s=80,label="Truck Start")
    plt.scatter(end[0],end[1],color="red",s=80,label="Dump Spot")
    plt.plot([start[0],end[0]],[start[1],end[1]],linestyle="--")

plt.title("AI Sequential Dump Planner (Option-2)")
plt.axis("equal")

print("Simulation Complete — Close graph window to end program")

plt.show(block=True)
input("Press Enter to exit...")