from collections import deque
# Goal-Based Agent
class FloodEscapeAgent:
    def __init__(self):
        # Environment (City Map)
        self.city_map = {
            "Home": ["Market", "School"],
            "Market": ["Home", "Hospital"],
            "School": ["Home", "Park"],
            "Hospital": ["Market", "Bridge"],
            "Bridge": ["Hospital"],
            "Park": ["School", "Relief Camp"],
            "Relief Camp": []
        }
        # Goal
        self.goal = "Relief Camp"
        # Flooded Roads
        self.flooded_roads = {
            ("Home", "Market"),
            ("Bridge", "Hospital")
        }
    # Check whether the road is flooded
    def is_flooded(self, a, b):
        return (a, b) in self.flooded_roads or (b, a) in self.flooded_roads
    # Find safe path using BFS
    def find_path(self, start):
        queue = deque([[start]])
        visited = set()
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == self.goal:
                return path
            if node not in visited:
                visited.add(node)

                for neighbour in self.city_map[node]:
                    if not self.is_flooded(node, neighbour):
                        queue.append(path + [neighbour])
        return None
    # Run Agent
    def run(self):
        start = input("Enter Current Location (Home/Market/School/Hospital/Park): ")
        if start not in self.city_map:
            print("Invalid Location")
            return
        print("\nGoal :", self.goal)
        print("Planning Safe Route...\n")
        path = self.find_path(start)
        if path:
            print("Safe Path Found")
            print(" -> ".join(path))
            print("\nMoving...")
            for place in path:
                print(place)

            print("\nGoal Achieved!")
            print("Citizens reached the Relief Camp safely.")

        else:
            print("No Safe Route Available.")
# Main Program
agent = FloodEscapeAgent()
agent.run()
