from modules.node import NodeLab


class Labyrinth:

    def __init__(self, labyrinth) -> None:
        self._labyrinth = labyrinth
        self.first_node = NodeLab((0, 1), "h", 0)   # Initial node

        # We would have finished if we reach one of these nodes
        self.stop_nodes = [NodeLab((len(labyrinth)-2, len(labyrinth[0])-1), "v", 0),
                           NodeLab((len(labyrinth)-1, len(labyrinth[0])-2), "h", 0)] 
        
    def heuristic(self, node : NodeLab) -> int:
        return (len(self._labyrinth) - node._pos[0]) + (len(self._labyrinth[0]) - node._pos[1]) # Manhattan distance to bottom-right corner
    
    def get_neighbors(self, node : NodeLab):

        neighbors = []

        for move in node.get_available_moves(self._labyrinth):

            if move == "right":
                neighbors.append(NodeLab(pos=(node._pos[0], node._pos[1] + 1), cost=node._cost + 1, direction=node._direction))
            elif move == "down":
                neighbors.append(NodeLab(pos=(node._pos[0] + 1, node._pos[1]), cost=node._cost + 1, direction=node._direction))
            elif move == "up":
                neighbors.append(NodeLab(pos=(node._pos[0] - 1, node._pos[1]), cost=node._cost + 1, direction=node._direction))
            elif move == "left":
                neighbors.append(NodeLab(pos=(node._pos[0], node._pos[1] - 1), cost=node._cost + 1, direction=node._direction))
            elif move == "rotate":
                neighbors.append(NodeLab(pos=(node._pos[0], node._pos[1]), cost=node._cost + 1, direction= "h" if node._direction == "v" else "v"))

        return neighbors



    def simple_a_star(self) -> int:
        open_set = set([self.first_node])   # Start with initial node
        closed_set = set()  # No nodes visited

        while len(open_set) > 0:    # While we can visit nodes

            expanding_node = None

            # Use heuristics to improve performance, finding the most promising node we can expand
            for v in open_set: 
                if expanding_node == None or v._cost + self.heuristic(v) < expanding_node._cost + self.heuristic(expanding_node):
                    expanding_node = v

            if expanding_node in self.stop_nodes:   # Goal found
                return expanding_node._cost
            elif not expanding_node:    # Can't keep expanding, no more available nodes
                return -1
            else:   # Not finished, but we can get new nodes

                for child in self.get_neighbors(expanding_node):
                    if child not in open_set and child not in closed_set:   # If not expanded before and not visited
                        open_set.add(child)     # Add to visit in the future

                closed_set.add(expanding_node)  # Add to mark as visited
                open_set.remove(expanding_node) # Remove to avoid expanding again
        
        return -1