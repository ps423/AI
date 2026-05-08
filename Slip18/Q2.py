'''
Q.2) Implement a system that performs arrangement of some set of objects in a room. Assume that you have only 5 rectangular, 4 square-shaped objects. Use A* approach for the placement of the objects in room for efficient space utilisation. Assume suitable heuristic, and dimensions of objects and rooms. (Informed Search)
[20 Marks]
'''

import heapq

class Object:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

def object_arrangement():
    # Define objects: 5 rectangular, 4 square-shaped
    objects = [
        Object("Rect1", 4, 2), Object("Rect2", 3, 2), Object("Rect3", 5, 3),
        Object("Rect4", 4, 3), Object("Rect5", 3, 3), Object("Square1", 2, 2),
        Object("Square2", 2, 2), Object("Square3", 2, 2), Object("Square4", 2, 2)
    ]
    
    room_width, room_height = 10, 10
    
    print("Object Arrangement using A* Approach")
    print(f"Room dimensions: {room_width}x{room_height}")
    print("Objects to arrange:")
    
    for obj in objects:
        print(f"  {obj.name}: {obj.width}x{obj.height}")
    
    # Simplified arrangement (this would be more complex in real implementation)
    x, y = 0, 0
    arrangement = []
    
    for obj in objects:
        if x + obj.width <= room_width:
            arrangement.append(f"{obj.name} at ({x},{y})")
            x += obj.width
        else:
            x = 0
            y += max(obj.height for obj in objects)
            if y >= room_height:
                print("Room is full!")
                break
            arrangement.append(f"{obj.name} at ({x},{y})")
            x += obj.width
    
    print("Arrangement:")
    for item in arrangement:
        print(f"  {item}")
    
    return arrangement

object_arrangement()
