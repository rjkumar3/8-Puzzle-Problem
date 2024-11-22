_goal_state = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]

class EightPuzzle:
    # (Keep the existing implementation of the EightPuzzle class here)
    # Methods: __init__, __eq__, __str__, _clone, _get_legal_moves, 
    # _generate_moves, _generate_solution_path, shuffle, find, peek, 
    # poke, swap should remain the same.

    def ids_solve(self):
        """
        Performs Iterative Deepening Search (IDS) for the goal state.
        Returns the solution path and the number of moves explored.
        """
        depth = 0
        move_count = 0
        
        while True:
            try:
                result, moves = self._dls(depth)
                move_count += moves
                if result:
                    return result, move_count
                depth += 1
            except RecursionError as e:
                print(f"Recursion depth exceeded at depth {depth}: {e}")
                break
            except Exception as e:
                print(f"An error occurred during IDS: {e}")
                break

    def _dls(self, limit):
        """
        Depth-Limited Search (DLS)
        limit - depth limit
        Returns the solution path if found within the limit, else None.
        """
        try:
            return self._recursive_dls(limit, 0, [])
        except Exception as e:
            print(f"An error occurred during DLS with limit {limit}: {e}")
            return None, 0

    def _recursive_dls(self, limit, depth, path):
        """
        Recursively performs depth-limited search.
        """
        try:
            if self.adj_matrix == _goal_state:
                return [path], 1
            
            if depth == limit:
                return None, 1
            
            move_count = 0
            for move in self._generate_moves():
                new_path = path + [move]
                result, moves = move._recursive_dls(limit, depth + 1, new_path)
                move_count += moves
                if result:
                    return result, move_count
            
            return None, move_count
        except Exception as e:
            print(f"An error occurred during recursive DLS at depth {depth}: {e}")
            return None, 0

def main():
    try:
        p = EightPuzzle()
        p.shuffle(20)
        print(p)

        path, count = p.ids_solve()
        if path:
            for state in path[0]:
                print(state)
            print(f"Solved with IDS exploring {count} states")
        else:
            print("No solution found within the given depth limit")
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()